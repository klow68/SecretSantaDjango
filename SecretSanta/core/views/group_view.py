# from django.shortcuts import get_object_or_404, render
# from .models import Question
from django.shortcuts import render
# from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..controller.group_controller import Group_controller
from ..model.form_model import Create_group_form
from ..model.form_model import EmailFormset
# from ..ressources.text_messages import Messages

""" CREATE GROUP """


@login_required
def create_group_form(request):

    if request.method == 'POST':
        form = Create_group_form(request.POST)
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # check if fields are valid
            if form.is_valid():
                # process the data in form.cleaned_data as required
                variables, user = Group_controller().create_group(form, request)

                # redirect to a new URL
                return redirect('/', variables)
    else:
        # create a form instance and populate it with data from the request
        form = Create_group_form()

    # if a GET (or any other method) we'll create a blank form
    variables = {"form": form}
    return render(request, 'core/create_group.html', variables)


@login_required
def create_group_user(request):
    template_name = 'core/email_group.html'
    if request.method == 'GET':
        formset = EmailFormset(request.GET or None)
    elif request.method == 'POST':
        formset = EmailFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save all email
                if name:
                    # Book(name=name).save()
                    print("Sucess")
            # once all email are saved, redirect to home
            return redirect('home')
    return render(request, template_name, {
        'formset': formset,
    })
