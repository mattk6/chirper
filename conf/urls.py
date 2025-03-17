# urls.py
# Grant Wells, Matthew Kruse
# Base urls for landing page, admin site, and chirper app
# 16 March 2025

"""
URL configuration for user login/logout flow & account signup
"""
from django.urls import path
from django.urls import include
from django.views.generic import TemplateView
from chirper import views

urlpatterns = [
    # url for main entry point
    path("", include("home.urls")),  
    # urls for built-in authentication
    path('accounts/', include('django.contrib.auth.urls')),
    # signup page
    path('accounts/signup/', views.signup, name='signup'),  
    # target page for logged out users
    path('accounts/logged_out/', TemplateView.as_view(template_name='registration/logged_out.html'), name='logged_out'),
]
