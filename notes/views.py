from django.shortcuts import render, get_object_or_404
from .models import StickyNote

# Create your views here.


def note_list(request):
    notes = StickyNote.objects.all()

    context = {
        "notes": notes,
        "note_title": "List of Notes",
    }

    return render(request, "notes/note_list.html", context)


def note_detail(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})
