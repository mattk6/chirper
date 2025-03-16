from django.urls import path
from . import views

app_name = 'chirper'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/chirp/', views.post_chirp, name='post_chirp'),
    path('profile/chirp/<int:chirp_id>/like/', views.like_chirp, name='like_chirp'),

    path('profile/chirp/<int:chirp_id>/reply/', views.reply_to_chirp, name='reply_to_chirp'),
]