from django import forms
from django.forms import formset_factory
from django.forms import ModelForm
# from django.core.mail import send_mail
from django.contrib.auth.models import User
from ..models import Secret_santa_group

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


class Create_group_form(ModelForm):
    class Meta:
        model = Secret_santa_group
        fields = ('group_name',)


class Email_form(forms.Form):
    name = forms.EmailField(
        label='name',
        widget=forms.TextInput(attrs={'class': 'form-control'}))


EmailFormset = formset_factory(Email_form, extra=1)


class Create_group_user(ModelForm):
    number_participants = forms.IntegerField()

    def __init__(self, fields, *args, **kwargs):
        super(Create_group_user, self).__init__(*args, **kwargs)
        for i in range(fields):
            self.fields['email_%i' % i] = forms.EmailField()

    def clean(self):
        cleaned_data = super(Create_group_user, self).clean()
        email_dict = {}
        for i in range(self.number_participants):
            email_dict["email_%i" % i] = cleaned_data["email_%i" % i]

        self.number_participants, email_dict = Valid_form.clean_duplicates(email_dict)

        for i in range(self.number_participants):
            cleaned_data["email_%i" % i] = email_dict["email_%i" % i]

        # TODO validate email 1 is user email


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
