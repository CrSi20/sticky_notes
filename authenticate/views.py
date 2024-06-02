from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout
from .forms import RegisterForms


# Create your views here.


def register_user(request):
    """A view function corresponding to the page to register
    a user

        Parameters:
            - request - the Http request
    """
    if request.method == "POST":
        form = RegisterForms(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            password_confirm = form.cleaned_data["password_confirm"]
            if password == password_confirm:
                new_user = User()
                new_user.username = form.cleaned_data["username"]
                new_user.set_password(password)
                new_user.save()
                if request.POST['account_type'] == 'poster':
                    group = Group.objects.get(name='posters')
                elif request.POST['account_type'] == 'reader':
                    group = Group.objects.get(name='readers')
                new_user.groups.add(group)
                login(request, new_user)
                return redirect("note_list")
    form = RegisterForms()
    return render(request, "registration/register.html", 
                  context={"form": form})


def logout_user(request):
    """A view function corresponding to the logout functionality

    Parameters:
        - request - the Http request
    """
    logout(request)
    return redirect('login')
