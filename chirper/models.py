# models.py
# Matthew Kruse, Grant Wells, David Marin
# Models for the database. Includes Chirp, and Like
# Last Updated: March 19, 2025


from django.db import models
from django.conf import settings

class Chirp(models.Model):
    """
    Model representing a Chirp.

    Attributes:
        user (ForeignKey): The user who created the chirp.
        message (CharField): The content of the chirp.
        created_at (DateTimeField): The timestamp when the chirp was created.
        likes (IntegerField): The number of likes the chirp has received.
        parent (ForeignKey): The parent chirp if this is a reply.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        """
        String representation of the Chirp model.

        Returns:
            str: A string representing the chirp.
        """
        return f"{self.user.username}: {self.message[:30]}..."

    class Meta:
        ordering = ['-created_at']

#### Testing likes model
class Like(models.Model):
    """
    Model representing a Like for a Chirp.
    Each user can like a chirp only once.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chirp = models.ForeignKey(Chirp, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'chirp')  # Ensure that each user can like a chirp only once

    def __str__(self):
        return f"{self.user.username} liked {self.chirp.message[:20]}"
