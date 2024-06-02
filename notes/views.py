from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import NoteForm
from .models import StickyNote


@login_required
def note_list(request):
    """A view function corresponding to the page showing the list
    of sticky notes

        Parameters:
            - request - the Http request
    """
    notes = StickyNote.objects.all()

    context = {
        "notes": notes,
        "note_title": "List of Notes",
    }

    return render(request, "notes/note_list.html", context)


@login_required
def note_detail(request, pk):
    """A view function corresponding to the page showing the content
    of a sticky note

        Parameters:
            - request - the Http request
            - pk - the primary key of the sticky note
    """

    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


@permission_required("notes.change_stickynote", login_url="note_list")
def note_update(request, pk):
    """A view function corresponding to the page to update a
    sticky note

        Parameters:
            - request - the Http request
            - pk - the primary key of the sticky note
    """
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
    """A view function corresponding to the page to create a
    sticky note

        Parameters:
            - request - the Http request
    """
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
    """A view function corresponding to the page to delete a
    sticky note

        Parameters:
            - request - the Http request
            - pk - the primary key of the sticky note
    """
    note = get_object_or_404(StickyNote, pk=pk)
    note.delete()
    return redirect("note_list")
