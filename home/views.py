from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home/index.html")



@login_required  # Ensure that the user is logged in before accessing the profile
def profile_view(request):
    return render(request, 'profile.html')