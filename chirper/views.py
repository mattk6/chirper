from django.shortcuts import render, redirect
from .models import Chirp
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

import pdb

@csrf_exempt
@login_required
def post_chirp(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            chirp = Chirp.objects.create(user=request.user, message=message)
            return JsonResponse({
                'id': chirp.id,
                'username': chirp.user.username,
                'message': chirp.message,
                'created_at': chirp.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'likes' : chirp.likes,
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


@csrf_exempt
@login_required
def post_reply(request, chirp_id):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            parent_chirp = Chirp.objects.get(pk=chirp_id)
            reply = Chirp.objects.create(user=request.user, message=message, parent=parent_chirp)
            return redirect('profile')  # Redirect to the profile page
        return JsonResponse({'error': 'No message provided'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)