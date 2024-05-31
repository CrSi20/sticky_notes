from django import forms
from .models import StickyNote

class NoteForm(forms.ModelForm):
    class Meta:
        model = StickyNote
        fields = ['title', 'content', 'author']