from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/chirp/', views.post_chirp, name='post_chirp'),
    path('profile/chirp/<int:chirp_id>/like/', views.like_chirp, name='like_chirp'),
    path('profile/chirp/<int:chirp_id>/reply/', views.post_reply, name='post_reply'),
]