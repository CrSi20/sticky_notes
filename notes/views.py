from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import NoteForm
from .models import StickyNote


# Create your views here.


@login_required
def note_list(request):
    notes = StickyNote.objects.all()

    context = {
        "notes": notes,
        "note_title": "List of Notes",
    }

    return render(request, "notes/note_list.html", context)


@login_required
def note_detail(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


@permission_required("notes.change_stickynote", login_url="note_list")
def note_update(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


@permission_required("notes.add_stickynote", login_url="note_list")
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            if request.user.is_authenticated:
                note.author = request.user
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm()
        return render(request, "notes/note_form.html", {"form": form})


@login_required
def note_delete(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    note.delete()
    return redirect("note_list")
