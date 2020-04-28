# from django.shortcuts import get_object_or_404, render
# from .models import Question
from django.shortcuts import render
# from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..controller.user_controller import user_controller
from ..model.form_model import Form

""" SIGN IN """


class Login_view():

    def sign_in(request):
        if request.method == 'POST':
            username = request.POST.get('username', False)
            password = request.POST.get('password', False)

            # controller actions
            variables = user_controller.login_user(request, username, password)

            print(variables)
            return render(request, "core/index.html", variables)
        return redirect("/")

    """ SIGN OUT """

    @login_required
    def sign_out(request):
        def get(self, request, **kwargs):
            user_controller.logout_user(request)
            return render(request, 'core/index.html')

        user_controller.logout_user(request)
        return render(request, 'core/index.html')

    """ CREATE USER """

    # show create user form page
    def create_user_view(request):
        return render(request, 'core/create_user.html')

    # @user_passes_test(email_check)
    def create_user(request):
        if request.method == 'POST':
            # get form informations
            form = Form()
            form.username = request.POST.get('username', False)
            form.email = request.POST.get('email', False)
            form.password = request.POST.get('password', False)
            form.password2 = request.POST.get('password2', False)
            form.first_name = request.POST.get('first_name', False)
            form.last_name = request.POST.get('last_name', False)

            # controller actions
            variables, user = user_controller.create_user(form)

            return render(request, 'core/index.html', variables)
        return render(request, 'core/create_user.html')


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
