from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote
from .forms import NoteForm

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

def note_update(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            if request.user.is_authenticated:
                note.author = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
        return render(request, 'notes/note_form.html', {'form': form})
    
def note_delete(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    note.delete()
    return redirect('note_list')

