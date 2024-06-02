from django import forms
from .models import StickyNote


class NoteForm(forms.ModelForm):
    """Class used to represent a form to create and update
    a sticky note.
    """

    class Meta:
        model = StickyNote
        fields = ['title', 'content', 'author']