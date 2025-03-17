# urls.py
# Matthew Kruse
# URLs for the chirper app
# 16 March 2025

"""
URL configuration for the chirper app
"""
from django.urls import path
from . import views

app_name = 'chirper'

urlpatterns = [
    # url for main app page with authenticated user 
    path('profile/', views.profile, name='profile'),
    # post chirp url
    path('profile/chirp/', views.post_chirp, name='post_chirp'),
    # like chirp url
    path('profile/chirp/<int:chirp_id>/like/', views.like_chirp, name='like_chirp'),
    # reply to chirp url
    path('profile/chirp/<int:chirp_id>/reply/', views.reply_to_chirp, name='reply_to_chirp'),
]
