from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .models import Question,Choice
from django.urls import reverse

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context={
            'latest_question_list':latest_question_list,
    }
    #output=', '.join([q.question_test for q in latest_question_list])
    return HttpResponse(template.render(context,request))
def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})
def results(request,question_id):
    response="You're looking at the results of question %s."
    return HttpResponse(response%question_id)
def vote(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(requset,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.'",
            })
    else:
        selected_choice.votes+=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
# Create your views here.
