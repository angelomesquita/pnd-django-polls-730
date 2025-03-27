from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Question “index” page – displays the latest few questions.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = { "latest_question_list": latest_question_list }
    return HttpResponse(template.render(context, request))

# Question “detail” page – displays a question text, with no results but with a form to vote.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

# Question “results” page – displays results for a particular question.
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# Vote action – handles voting for a particular choice in a particular question.
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)