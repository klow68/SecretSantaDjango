from django import forms
from django.forms import BaseInlineFormSet
from django.forms import ModelForm
# from django.core.mail import send_mail
from django.contrib.auth.models import User
from ..models import Secret_santa_group, Secret_santa_group_user
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_formset import Formset
""" Form class to be used for all forms of the website """


""" TODO remove """


class Login_form(forms.Form):
    username = forms.CharField(label='Utilisateur', max_length=100)
    password = forms.CharField(label='Mot de passe', max_length=32, widget=forms.PasswordInput)


class Create_user_form(ModelForm):
    password = forms.CharField(label='Mot de passe', max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Mot de passe', max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        cleaned_data = super(Create_user_form, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        Valid_form().is_same_password(password, confirm_password)


""" groups """

class Create_group_form(forms.ModelForm):

    class Meta:
        model = Secret_santa_group_user
        exclude = ()


class BaseSecret_santa_groupFormSet(BaseInlineFormSet):
    def clean(self):
        """forces each clean() method on the ChildCounts to be called"""
        super(BaseInlineFormSet, self).clean()

        """Checks that no two articles have the same title."""
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return
        # check if there is duplicated and empty emails
        emails = []
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue

            email = form.cleaned_data.get('email')

            if not email or email == "":
                raise forms.ValidationError("Un email est vide", "error")

            if email in emails:
                raise forms.ValidationError("Les emails doivent être différents", "error")
            emails.append(email)


class GroupForm(forms.ModelForm):

    class Meta:
        model = Secret_santa_group
        exclude = ('master_user', 'creation_date')

    def __init__(self, is_update, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.is_update = is_update
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('group_name'),
                Fieldset('Email', Formset('formset')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
        )

    def clean_group_name(self):
        group_name = self.cleaned_data['group_name']
        group = Secret_santa_group.objects.filter(group_name=group_name)

        if group and not self.is_update:
            raise forms.ValidationError("Ce groupe existe déjà", "error")
        return group_name


""" Validation forms tests """


class Valid_form():

    # check if two password are the same
    def is_same_password(self, password, confirm_password):
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match", code='42'
            )

    # clean all duplicate in dict and return a new dict and the size of it
    def clean_duplicates(self, dict):
        new_dict = ()
        cpt = 0
        for key, value in dict.items():
            if value not in new_dict.values() and not "":
                new_dict[key] = value
                cpt += 1

        return cpt, new_dict


"""
# example for sending mail
def is_mail_valid(self, form):
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']

    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    # return HttpResponseRedirect('/thanks/')
    return "TODO"
"""
