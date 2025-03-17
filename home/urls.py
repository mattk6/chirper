# urls.py
# Grant Wells, Matthew Kruse
# Base urls for landing page, admin site, and chirper app
# 16 March 2025

"""
URL configuration for the home app, admin site, direction to chirper
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import profile_view

urlpatterns = [
    # home / site landing page
    path("", views.home, name="home"),  
    # landing page for authenticated users
    path("profile/", profile_view, name="profile"),
    # admin site for user maintenance
    path('admin/', admin.site.urls), 
    # chirper app urls
    path('chirps/', include('chirper.urls')), 
]