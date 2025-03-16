from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChirpForm, ReplyForm, CustomUserCreationForm
from .models import Chirp
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string

def profile(request):
    chirps = Chirp.objects.filter(parent=None).order_by('-created_at')  # Filter for chirps with no parent
    if request.method == 'GET':
        form = ChirpForm()
    else:
        form = None
    context = {'chirps': chirps, 'form': form}
    return render(request, 'home/profile.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def post_chirp(request):
    if request.method == "POST":
        form = ChirpForm(request.POST)
        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.user = request.user
            chirp.save()
            return redirect('chirper:profile')  # Namespaced redirect
        else:
            return render(request, 'home/profile.html', {'form': form})
    else:
        form = ChirpForm()
        return render(request, 'home/profile.html', {'form': form})

@login_required
def like_chirp(request, chirp_id):
    if request.method == 'POST':
        chirp = get_object_or_404(Chirp, id=chirp_id)
        chirp.likes += 1
        chirp.save()

    if request.headers.get('HX-Request'):
        html = render_to_string('partials/like_count.html', {'chirp': chirp})
        return HttpResponse(html)

    return redirect('chirper:profile')  # Namespaced redirect

@login_required
def reply_to_chirp(request, chirp_id):
    parent_chirp = get_object_or_404(Chirp, id=chirp_id)
    print(f"Parent chirp ID: {parent_chirp.id}")

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.parent = parent_chirp
            reply.save()

            print(f"Reply message: {reply.message}")
            print(f"Reply parent ID: {reply.parent.id}")

            print("Reply created")
            if request.headers.get('HX-Request'):
                # Return the HTML for the new reply for HTMX requests
                return render(request, 'partials/reply.html', {'reply': reply})
            else:
                return redirect('chirper:profile')
        else:
            print(f"Form errors: {form.errors}")
            return render(request, 'home/profile.html', {'form': form, 'parent_chirp': parent_chirp})
    else:
        form = ReplyForm()
        return render(request, 'home/profile.html', {form: form, 'parent_chirp': parent_chirp})