# from django.shortcuts import get_object_or_404, render
# from .models import Question
from django.shortcuts import render
# from django.http import Http404
from ..ressources.text_messages import Messages
from ..model.form_model import Login_form
from ..models import Secret_santa_group


# todo show message user created
def index(request):
    if request.user.is_authenticated:
        # Logged in
        group_list = Secret_santa_group.objects.filter(master_user=request.user)

        variables = {"group_list": group_list}
    else:
        # not logged in
        if request.method == 'POST':
            form = Login_form(request.POST)
        else:
            form = Login_form()
        variables = {"form": form}

    return render(request, 'core/index.html', variables)
