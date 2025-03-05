from django.urls import path
from . import views
from .views import profile_view

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", profile_view, name="profile"),
]
