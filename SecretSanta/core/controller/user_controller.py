from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ..ressources.text_messages import Messages


class User_controller():

    # create a new user
    def create_user(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']

        # Create user and save to the database
        user = User.objects.create_user(username, email, password)

        # Update fields and then save again
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        variables = {"messages": ["Your user " + username + " has been created"]}
        return variables, user

    def login_user(self, request, form):

        is_logged = False

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        variables = {"form": form, "errors": [Messages.errors['login_error']]}

        if user is not None and user.is_active:
            login(request, user)
            is_logged = True
            variables = {}
        return variables, is_logged

    def logout_user(self, request):
        logout(request)
