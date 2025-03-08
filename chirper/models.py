from django.db import models
from django.contrib.auth.models import User  

class Chirp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    message = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True) 
    likes = models.IntegerField(default=0)  # Add this line
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"{self.user.username}: {self.message[:30]}..." 

    class Meta:
        ordering = ['-created_at']