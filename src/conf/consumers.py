import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
from asgiref.sync import sync_to_async


class ChirpConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("chirps", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("chirps", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")
        chirp_id = text_data_json.get("chirp_id")
        username = self.scope["user"].username
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"Received message from {username}: {message} at {timestamp}")

        if message:
            event_dict = {
                "type": "chirp_message",
                "message": message,
                "username": username,
                "timestamp": timestamp,
            }

            print(f"Event dictionary in receive: {event_dict}")

            await self.channel_layer.group_send("chirps", event_dict)

        if chirp_id:
            from chirper.models import Chirp

            # Make the database call asynchronous
            chirp = await Chirp.objects.aget(id=chirp_id)
            chirp.likes += 1
            await chirp.asave()

            # Broadcast the updated like count to all connected clients
            await self.channel_layer.group_send(
                "chirps",
                {
                    "type": "update_like_count",
                    "chirp_id": chirp_id,
                    "likes": chirp.likes,
                },
            )

    async def chirp_message(self, event):
        message = event["message"]
        username = event.get("username")
        timestamp = event.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        print(f"Event received in chirp_message: {event}")

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                    "timestamp": timestamp,
                }
            )
        )

    async def update_like_count(self, event):
        chirp_id = event["chirp_id"]
        likes = event["likes"]

        await self.send(text_data=json.dumps({"chirp_id": chirp_id, "likes": likes}))