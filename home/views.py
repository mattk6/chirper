# views.py
# Grant Wells, Matthew Kruse
# Views for home page and profile page
# 16 March 2025

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chirper.models import Chirp

"""
Render the home page.

Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
"""

def home(request):
    return render(request, "home/home.html")

@login_required
def profile_view(request):
    """
    Render the profile page with the user's chirps.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered profile page with chirps.
    """
    chirps = Chirp.objects.all()
    return render(request, 'home/profile.html', {'chirps': chirps, 'user': request.user})