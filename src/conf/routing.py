from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chirps/', consumers.ChirpConsumer.as_asgi()),
]