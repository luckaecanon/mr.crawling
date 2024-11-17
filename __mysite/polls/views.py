# для специальных быстрых дейсвтий
from django.shortcuts import render
from django.http import HttpResponse  # мы подключаем HttpResponse

# импортируем таблицу
from .models import Question

# импортировать обработчик шаблонов django
from django.template import loader

# Create your views here.


# 127. .../polls/
def index(request):
    my_var = "это какой-то текст"
    latest_question_list = Question.objects.order_by("-pub_date")[:4]
    #output = "----".join([q.question_text for q in latest_question_list])
    template = loader.get_template("polls/fck.html")
    context = {
        "latest_question_list": latest_question_list,
        "my_var": my_var,
    }
    return HttpResponse(template.render(context, request))


# 127. .../polls/details
def detail(request, question_id):
    question = Question.object.get(pk=question_id)
    template = loader.get_tamplate("polls/detail.html")
    context = {
        "question": question,
    }
    return HttpResponse("Вы просматриваете опросы %s." % question_id)


# 127. .../polls/results
def results(request, question_id):
    response = "Вы просматриваете результаты опросов %s." % question_id
    return HttpResponse(response % question_id)


# 127. .../polls/vote
def vote(request, question_id):
    return HttpResponse("Вы просматриваете варианты выбора в опроснике" % question_id)

# for question in Question.objects:
#     print(question.question_text)

# http://127.0.0.1:8000/polls/

from django.shortcuts import render
from django.hhtp import HttpResponse

def hello(request):
    return HttpResponse


