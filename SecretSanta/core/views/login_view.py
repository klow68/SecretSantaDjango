# from django.shortcuts import get_object_or_404, render
# from .models import Question
from django.shortcuts import render
# from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..controller.user_controller import User_controller
from ..model.form_model import Create_user_form, Login_form
# from ..ressources.text_messages import Messages

""" SIGN IN """


def sign_in(request):

    # create a form instance and populate it with data from the request
    form = Login_form(request.POST)

    if request.method == 'POST':
        # check if fields are valid
        if form.is_valid():
            # controller actions
            variables, is_logged = User_controller().login_user(request, form)

            if is_logged:
                return redirect('/', variables)

    variables = {"form": form}
    return render(request, 'core/index.html', variables)


""" SIGN OUT """


@login_required
def sign_out(request):
    form = Login_form(request.POST)
    variables = {"form": form}

    def get(self, request, **kwargs):
        User_controller().logout_user(request)
        # TODO moodify to redirect
        return render(request, 'core/index.html', variables)

    User_controller().logout_user(request)
    return render(request, 'core/index.html', variables)


""" CREATE USER """


# @user_passes_test(email_check)
def create_user(request):

    # create a form instance and populate it with data from the request
    form = Create_user_form(request.POST)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # check if fields are valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            variables, user = User_controller().create_user(form)

            # redirect to a new URL
            return redirect('/', variables)

    # if a GET (or any other method) we'll create a blank form
    variables = {"form": form}
    return render(request, 'core/create_user.html', variables)


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
