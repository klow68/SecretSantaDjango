# from django.shortcuts import get_object_or_404, render
# from .models import Question
from django.shortcuts import render
# from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from . import text_messages
from django.contrib.auth.models import User


messages = text_messages.Messages()


def index(request):
    variables = {"messages": ["Welcome to Secret Satan"]}
    return render(request, 'secretSanta/index.html', variables)


def create_user_view(request):
    return render(request, 'secretSanta/create_user.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        form = {"errors": messages.errors['login_error']}

        if user is not None and user.is_active:
            login(request, user)
            form = {}

        variables = {'form': form}
        return render(request, "secretSanta/index.html", variables)
    return redirect("/")


@login_required
def sign_out(request):
    def get(self, request, **kwargs):
        logout(request)
        return render(request, 'secretSanta/index.html')

    logout(request)
    return render(request, 'secretSanta/index.html')


# todo check form
def check_password(password, password2):
    if (password == password2):
        return True


def is_form_valid(form):
    result = True
    form.errors = []

    if (form.password and form.password2):
        check_password(form.password, form.password2)
    else:
        form.errors += ["passwords are differents"]
        result = False

    return result


# todo messages error
# @user_passes_test(email_check)
def create_user(request):
    if request.method == 'POST':
        # if form.is_valid():
        form = Form()
        form.username = request.POST.get('username', False)
        form.email = request.POST.get('email', False)
        form.password = request.POST.get('password', False)
        form.password2 = request.POST.get('password2', False)
        form.first_name = request.POST.get('first_name', False)
        form.last_name = request.POST.get('last_name', False)

        if is_form_valid(form):

            # Create user and save to the database
            user = User.objects.create_user(form.username, form.email, form.password)

            # Update fields and then save again
            user.first_name = form.first_name
            user.last_name = form.last_name
            user.save()
            variables = {"messages": ["Your user " + form.username + " has been created"]}
            return render(request, 'secretSanta/index.html', variables)
        else:
            variables = {"messages": form.errors}
            return render(request, 'secretSanta/index.html', variables)
    return render(request, 'secretSanta/create_user.html')


# todo export this in an other file
class Form:
    username = ""
    password = ""
    password2 = ""
    email = ""
    first_name = ""
    last_name = ""
    errors = []


"""
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ...
"""
