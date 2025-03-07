from django.shortcuts import render, redirect
from .models import Chirp
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@csrf_exempt
@login_required
def post_chirp(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            chirp = Chirp.objects.create(user=request.user, message=message)

            # Notify via WebSocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "chirps",
                {
                    'type': 'chirp_message',
                    'message': message,
                }
            )

            return JsonResponse({
                'id': chirp.id,
                'username': chirp.user.username,
                'message': chirp.message,
                'likes': 0,
                'created_at': chirp.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        return JsonResponse({'error': 'No message provided'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
@login_required
def like_chirp(request, chirp_id):
    if request.method == 'POST':
        try:
            chirp = Chirp.objects.get(pk=chirp_id)
            chirp.likes += 1
            chirp.save()
            return JsonResponse({'likes': chirp.likes})
        except Chirp.DoesNotExist:
            return JsonResponse({'error': 'Chirp not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def profile_view(request):

    chirps = Chirp.objects.all()
    return render(request, 'home/profile.html', {'chirps': chirps, 'user': request.user})