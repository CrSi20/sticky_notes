from django.db import models


# Create your models here.
class StickyNote(models.Model):
    """Class representing a sticky note.

    Attributes:
        title: Charfield - The title of the sticky note
        content: TextField - The content of the sticky note
        created_at: DateTimeField - The DateTime sticky note is created
        author: Charfield - The author of the sticky note
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
