# chirper/views.py
# Grant Wells, Matthew Kruse, David Marin
# Views for chirper app, including signup, profile, and chirp actions
# Last Updated: March 19, 2025

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChirpForm, ReplyForm, CustomUserCreationForm
from .models import Chirp, Like
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string

def signup(request):
    """
    Handle user signup.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered signup page or redirect to login.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # If the form input is valid, save the user
        if form.is_valid():
            form.save()

            # Redirect to login page after successful signup
            return redirect('login')
    else:
        # reamin on the signup page if form input is invalid
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    """
    Render the profile page with chirps.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered profile page with chirps.
    """
    # Get all chirps that are not replies
    chirps = Chirp.objects.filter(parent=None).order_by('-created_at')
    form = ChirpForm()
    context = {'chirps': chirps, 'form': form}
    return render(request, 'home/profile.html', context)


@login_required
def post_chirp(request):
    """
    Handle posting a new chirp.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered profile page or redirect to profile.
    """

    # Process the form data if the request method is POST
    if request.method == "POST":
        form = ChirpForm(request.POST)
        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.user = request.user
            chirp.save()
            # Redirect to the profile page after posting a chirp
            return redirect('chirper:profile')
        else:
            # If the form is invalid, render the profile page again
            return render(request, 'home/profile.html', {'form': form})
    else:
        # A GET request renders the profile page with the form
        form = ChirpForm()
        return render(request, 'home/profile.html', {'form': form})


from django.template import RequestContext  # Import RequestContext

@login_required
def like_chirp(request, chirp_id):
    """
    Handles liking for chirps and replies. Ensures only one like per user.

    Args:
        request: The HTTP request object.
        chirp_id: The ID of the chirp to like.

    Returns:
        HttpResponse: The updated like count or redirect to profile.
    """
    # # Increase like count for the message identified by chirp_id
    # if request.method == 'POST':
    #     chirp = get_object_or_404(Chirp, id=chirp_id)
    #     chirp.likes += 1
    #     chirp.save()
    chirp = get_object_or_404(Chirp, id=chirp_id)

    # Check if user already liked chirp
    like, created = Like.objects.get_or_create(user=request.user, chirp=chirp)

    if not created:
        # If user liked chirp or reply already, delete user's like
        like.delete()
    else:
        # If user hasn't liked the chirp or reply yet, add the like by savving it
        like.save()

    # Recalculate the number of likes
    chirp.likes = Like.objects.filter(chirp=chirp).count()

    # Save updated count for likes
    chirp.save()

    # Perform HTMX processing to update the like count
    if request.headers.get('HX-Request'):
        html = render_to_string('partials/like_count.html', {'chirp': chirp})
        return HttpResponse(html)

    return redirect('chirper:profile')

@login_required
def reply_to_chirp(request, chirp_id):
    """
    Handle replying to a chirp.

    Args:
        request: The HTTP request object.
        chirp_id: The ID of the chirp to reply to.

    Returns:
        HttpResponse: The rendered reply or redirect to profile.
    """
    # Get the parent chirp
    parent_chirp = get_object_or_404(Chirp, id=chirp_id)

    # Only perform actions on POST requests
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.parent = parent_chirp
            reply.save()

            # Use HTMX to update the page
            if request.headers.get('HX-Request'):
                # Use the partials/reply.html template to render the reply
                return render(request, 'partials/reply.html', {'reply': reply})
            else:
                return redirect('chirper:profile')
        else:
            # If the form is invalid, render the profile page again
            return render(request, 'home/profile.html', {'form': form, 'parent_chirp': parent_chirp})
    else:
        # No POST is happening, render the profile page with the form
        form = ReplyForm()
        return render(request, 'home/profile.html', {form: form, 'parent_chirp': parent_chirp})