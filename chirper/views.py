from django.shortcuts import render


@login_required  # Ensure that the user is logged in before accessing the profile
def profile_view(request):

    user = request.user

    return render(request, 'home/profile.html', {'user': user})