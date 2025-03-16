from django.db import models

from django.conf import settings


class Chirp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    message = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True) 
    likes = models.IntegerField(default=0)  # Add this line

    def __str__(self):
        return f"{self.user.username}: {self.message[:30]}..." 

    class Meta:
        ordering = ['-created_at']