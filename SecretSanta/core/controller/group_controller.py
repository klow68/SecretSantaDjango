from django.contrib import messages
from ..models import Secret_santa_group
from ..models import Secret_santa_group_user

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

            self.create_group_user(group, current_user.email)

            for subform in formset:
                # extract email from each form and save
                email = subform.cleaned_data.get('email')

                # save all email
                if email:
                    self.create_group_user(group, email)

        messages.success(request, "Le groupe " + group_name + " crée")

    # update group
    # add and remove user conform of the informations of the form
    def update_group(self, form, formset, request):
        group_name = form.cleaned_data['group_name']
        updated = False
        emailList = []

        group = self.get_group(group_name, request)

        # update added email
        for subform in formset:
            # extract email from each form and save
            email = subform.cleaned_data.get('email')

            # save all email
            if email:
                emailList.append(email)
                # if group exist
                if group:
                    saved = self.create_group_user(group, email)
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

    # Remove a group and all the group users linked
    # check if the group_master is the current user
    def remove_group(self, group_name, request):
        # if the user is the master_user of the group
        group = self.get_group(group_name, request)

        if group:
            if group.master_user == request.user:
                # remove all group users of the group
                for group_user in Secret_santa_group_user.objects.filter(group=group):
                    group_user.delete()
                # remove the group
                group.delete()
                messages.success(request, "Le groupe " + group_name + " à été supprimé avec succès")
            else:
                messages.error(request, "Vous n'êtes pas le créateur du groupe")

    # GETTER

    def get_group(self, group_name, request):
        # get group with GET informations
        try:
            group = Secret_santa_group.objects.get(group_name=group_name)
            return group
        except Exception:
            messages.error(request, "Ce groupe n'existe pas")
            return None

    # get initial data for the update group form
    # return group , initial_data
    def get_initial_data(self, group_name, request):
        # get group with GET informations
        group = self.get_group(group_name, request)

        if group:
            # get all group user linked
            group_users = Secret_santa_group_user.objects.filter(group=group)

            # initiate all groupset
            initial_data = []
            for group_user in group_users:
                initial_data.append({'email': group_user.email},)

            return initial_data
        return None

    # OTHERS

    # create a group user with group and email
    # return if the group user has been saved in the database
    def create_group_user(self, group, email):
        saved = False

        # check if this email is already added to the group
        if not Secret_santa_group_user.objects.filter(group=group, email=email):
            # create group user
            group_user = Secret_santa_group_user.objects.create(group=group, email=email)
            group_user.save()
            saved = True
        return saved
