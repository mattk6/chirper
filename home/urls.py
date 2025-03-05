from django.contrib import admin
from django.urls import path, include
from . import views
from .views import profile_view
urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", profile_view, name="profile"),

    path('admin/', admin.site.urls),
    path('chirps/', include('chirper.urls')),  # Include chirp URLs
]