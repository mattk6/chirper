from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home/index.html")



def profile_view(request):
    user = request.user
    return render(request, 'home/profile.html', {'user': user})