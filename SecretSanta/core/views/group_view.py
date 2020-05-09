# from django.shortcuts import get_object_or_404, render
# from .models import Question
from django.shortcuts import render
# from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..model.form_model import GroupForm
from ..model.form_model import Secret_santa_groupFormSet
# from ..ressources.text_messages import Messages

""" CREATE GROUP """


@login_required
def create_group(request):
    template_name = 'core/email_group.html'
    form = GroupForm()
    if request.method == 'GET':
        formset = Secret_santa_groupFormSet()
    elif request.method == 'POST':
        formset = Secret_santa_groupFormSet(request.POST)
        if request.form.is_valid():
            for subform in formset:
                # extract name from each form and save
                name = subform.cleaned_data.get('email')
                # save all email
                if name:
                    print("Sucess")
            # once all email are saved, redirect to home
            return redirect('home')
    return render(request, template_name, {'formset': formset, 'form': form, })
