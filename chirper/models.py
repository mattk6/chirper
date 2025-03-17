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