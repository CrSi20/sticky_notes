from django.shortcuts import render
from .models import StickyNote

# Create your views here.

def note_list(request):
    notes = StickyNote.objects.all()

    context ={
        'notes': notes,
        'note_title': 'List of Notes',
    }

    return render(request, 'notes/note_list.html', context)