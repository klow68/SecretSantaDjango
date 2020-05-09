from ..models import Secret_santa_group
# from ..ressources.text_messages import Messages


class Group_controller():

    # create a new group
    def create_group(self, form, request):
        group_name = form.cleaned_data['group_name']
        email = request.POST.get('email0')
        print(email)

        # Create user and save to the database
        group = Secret_santa_group.objects.create(group_name=group_name, master_user=request.user)

        # Update fields and then save again
        group.save()

        variables = {"messages": ["Your group " + group_name + " has been created"]}
        return variables, group
