from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Choice
from django.http import HttpResponseRedirect
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your views here.

@csrf_exempt
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    output = '<head><link rel="stylesheet" href="' + static('polls/style.css') + '"></head> <ul>'
    for question in latest_question_list:
        output = output + '<li><a href="/polls/' +str(question.id) + '/">' + question.question_text + '</a></li>'
    output = output + "</ul>"
    return HttpResponse(output)

@csrf_exempt    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question_id = int(question_id)
    output = ""
    if question_id %10 == 1 and question_id != 11:
        output = "You're looking at the %sst question." % question_id
    elif question_id %10 == 2 and question_id != 12:
        output = "You're looking at the %snd question." % question_id
    elif question_id %10 == 3 and question_id != 13:
        output = "You're looking at the %srd question." % question_id
    else:
        output = "You're looking at the %sth question." % question_id
    output = "<h1>" + question.question_text + "</h1><p>" + output + "</p>"
    output = output + '<form action ="/polls/' + str(question_id) + '/vote/" method = "post">'
    count = 1
    for choice in question.choice_set.all():
        output = output + '<input type="radio" name = "choice" id="choice' + str(count) + '"value="' + str(choice.id) + '" />'
        output = output + '<label for="choice' + str(count) + '">' + choice.choice_text + '</label><br />'
        count += 1
    output = '<head><link rel="stylesheet" href="' + static('polls/style.css') + '"></head>' + output + '<input type="submit" value = "Vote" /></form>'
    return HttpResponse(output)

@csrf_exempt
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        user_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse("No choice selected.")
    else:
        user_choice.votes += 1
        user_choice.save()
    return HttpResponseRedirect("/polls/" + str(question_id) + "/results/")
    
@csrf_exempt
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    output = '<h1></pre>' + question.question_text + '</h1><ul>'
    for choice in question.choice_set.all():
        output = output + '<li>' + choice.choice_text + ' >>> ' + str(choice.votes)
    output = output + '</ul>'
    return HttpResponse(output)