from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chirper.models import Chirp

def home(request):
    return render(request, "home/index.html")

@login_required
def profile_view(request):

    chirps = Chirp.objects.all()
    return render(request, 'home/profile.html', {'chirps': chirps, 'user': request.user})