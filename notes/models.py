from django.db import models


# Create your models here.
class StickyNote(models.Model):
    """A note the user is learning about."""

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
