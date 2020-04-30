# from django.shortcuts import get_object_or_404, render
# from .models import Question
from django.shortcuts import render
# from django.http import Http404
from ..ressources.text_messages import Messages
from ..model.form_model import Login_form


class Index_view():

    # todo show message user created
    def index(request):
        form = Login_form(request.POST)
        variables = {"messages": [Messages.display['welcome']], "form": form}
        return render(request, 'core/index.html', variables)
