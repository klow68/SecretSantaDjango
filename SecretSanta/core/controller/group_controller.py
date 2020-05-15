from django.contrib import messages
from ..models import Secret_santa_group
from ..models import Secret_santa_group_user
# from ..ressources.text_messages import Messages


class Group_controller():

    # create a new group
    # check if group don't exist and add the user email
    # to the group and all the emails from the formset
    def create_group(self, form, formset, request):
        group_name = form.cleaned_data['group_name']

        group = Secret_santa_group.objects.filter(group_name=group_name)

        current_user = request.user
        # if group doesn't exist
        if not group:
            # Create group and save to the database
            group = Secret_santa_group.objects.create(group_name=group_name, master_user=request.user)
            group.save()

            create_group_user(group, current_user.email)

            for subform in formset:
                # extract email from each form and save
                email = subform.cleaned_data.get('email')

                # save all email
                if email:
                    create_group_user(group, email)

        messages.success(request, "Le groupe " + group_name + " crée")

    def update_group(self, form, formset, request):
        group_name = form.cleaned_data['group_name']
        updated = False
        emailList = []

        try:
            group = Secret_santa_group.objects.get(group_name=group_name)
        except Exception:
            group = None

        # update added email
        for subform in formset:
            # extract email from each form and save
            email = subform.cleaned_data.get('email')

            # save all email
            if email:
                emailList.append(email)
                # if group exist
                if group:
                    saved = create_group_user(group, email)
                    if saved:
                        updated = True

        # update removed email
        for group_user in Secret_santa_group_user.objects.filter(group=group):
            if group_user.email not in emailList:
                updated = True
                group_user.delete()

        if updated:
            messages.success(request, "Le groupe " + group_name + " a été mis à jour")
        else:
            messages.warning(request, "Aucune mise à jour")


def create_group_user(group, email):
    saved = False

    # check if this email is already added to the group
    if not Secret_santa_group_user.objects.filter(group=group, email=email):
        # create group user
        group_user = Secret_santa_group_user.objects.create(group=group, email=email)
        group_user.save()
        saved = True
    return saved
