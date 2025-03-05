from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/chirp/', views.post_chirp, name='post_chirp'),
]