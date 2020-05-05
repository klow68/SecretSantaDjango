# from django.shortcuts import get_object_or_404, render
# from .models import Question
from django.shortcuts import render
# from django.http import Http404
from ..ressources.text_messages import Messages
from ..model.form_model import Login_form
from django.conf import settings


# todo show message user created
def index(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
    else:
        form = Login_form()
    variables = {"form": form}
    return render(request, 'core/index.html', variables)
