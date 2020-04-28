from ..model.form_model import Form
from django.contrib.auth import authenticate, login, logout
from ..ressources.text_messages import Messages
from django.contrib.auth.models import User


class user_controller():

    def create_user(form):
        if Form.is_form_valid(form):

            # Create user and save to the database
            user = User.objects.create_user(form.username, form.email, form.password)

            # Update fields and then save again
            user.first_name = form.first_name
            user.last_name = form.last_name
            user.save()
            variables = {"messages": ["Your user " + form.username + " has been created"]}
            return variables, user
        else:
                variables = {"messages": form.errors}
                return variables, None

    def login_user(request, username, password):
        user = authenticate(username=username, password=password)
        variables = {"errors": [Messages.errors['login_error']]}

        if user is not None and user.is_active:
            login(request, user)
            variables = {}
        return variables

    def logout_user(request):
        logout(request)
