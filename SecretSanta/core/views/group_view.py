from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from ..model.form_model import GroupForm
from ..model.form_model import BaseSecret_santa_groupFormSet, Create_group_form
from ..controller.group_controller import Group_controller
from ..models import Secret_santa_group
from ..models import Secret_santa_group_user

Secret_santa_groupFormSet = inlineformset_factory(
    Secret_santa_group, Secret_santa_group_user,
    form=Create_group_form, extra=1,
    fields=['email'], formset=BaseSecret_santa_groupFormSet,)


# TODO why all user are not saved ? wtf

@login_required
def create_group(request):
    is_update = False
    template_name = 'core/create_group.html'

    if request.method == 'GET':
        form = GroupForm(is_update)
        formset = Secret_santa_groupFormSet()
    elif request.method == 'POST':
        form = GroupForm(is_update, request.POST)
        formset = Secret_santa_groupFormSet(request.POST)

        # validate form
        if form.is_valid():
            if formset.is_valid():
                Group_controller().create_group(form, formset, request)

                return redirect('home')
            else:
                # add fomrset errors messages to context
                for error in formset.non_form_errors():
                    messages.error(request, error)

    return render(request, template_name, {
        'formset': formset,
        'form': form
    })


@login_required
def update_group(request, group_name):
    is_update = True
    template_name = 'core/create_group.html'

    if request.method == 'GET':
        # get group with GET informations
        try:
            group = Secret_santa_group.objects.get(group_name=group_name)
        except Exception:
            messages.error(request, "Plus d'un groupe possède ce nom !")
            return redirect('home')
        # get all group user linked
        group_users = Secret_santa_group_user.objects.filter(group=group)

        # initiate groupForm
        form = GroupForm(is_update, initial={"group_name": group.group_name})
        # initiate all groupset
        initial_data = []
        for group_user in group_users:
            initial_data.append({'email': group_user.email},)

        # create formset with extra at the right value
        formset = inlineformset_factory(
            Secret_santa_group, Secret_santa_group_user,
            form=Create_group_form,
            fields=['email'], formset=BaseSecret_santa_groupFormSet,
            extra=len(initial_data), can_delete=True)
        formset = formset(initial=initial_data)

    elif request.method == 'POST':
        form = GroupForm(is_update, request.POST)
        formset = Secret_santa_groupFormSet(request.POST)

        # validate form
        if form.is_valid():
            if formset.is_valid():
                Group_controller().update_group(form, formset, request)

                return redirect('home')
            else:
                # add fomrset errors messages to context
                for error in formset.non_form_errors():
                    messages.error(request, error)

    form.fields['group_name'].widget.attrs['readonly'] = True

    return render(request, template_name, {
        'formset': formset,
        'form': form
    })
