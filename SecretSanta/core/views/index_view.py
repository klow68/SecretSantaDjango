# from django.shortcuts import get_object_or_404, render
# from .models import Question
from django.shortcuts import render
# from django.http import Http404
from ..ressources.text_messages import Messages

messages = Messages


class Index_view():
    def index(request):
        variables = {"messages": [Messages.display['welcome']]}
        return render(request, 'core/index.html', variables)
