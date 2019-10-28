from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator
from django.template import loader
# Create your views here.
#powtórz sobie generyczne templatki
#wybrać obsługiwany indeks
def index(request):
    questions = Question.objects.order_by("-pub_date")[:6]
    #template = loader.get_template("polls/index.html")
    context = {
        'questions': questions
    }
    #return HttpResponse(template.render(context, request))
    return render(
        request = request,
        context = context,
        template_name = "polls/index.html"
    )
def index2(request):
    question_list = Question.objects.all()
    #template = loader.get_template("polls/index.html")
    paginator = Paginator(question_list, 20)
    page = request.GET.get("page")
    questions =  paginator.get_page(page)
    context = {
        'questions': questions
    }
    #return HttpResponse(template.render(context, request))
    return render(
        request = request,
        context = context,
        template_name = "polls/index.html"
    )
def detail(request, question_id):
    #można try except + raise http404 i odniesienie
    question = get_object_or_404(Question, pk=question_id)
    #output = "Jesteś na stronie szczegółów pytania %s" % question_id
    #output += str(question)
    context = {
        'question': question
    }
    return render(
        request=request,
        context=context,
        template_name="polls/details.html"
    )


class IndexView(generic.ListView):
    model = Question
    context_object_name = "questions"
    template_name = "polls/index.html"

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question
    }
    return render(
        request=request,
        context=context,
        template_name="polls/results.html"
    )

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice_id = request.POST['choice']
    selected_choice = question.choice_set.get(pk=selected_choice_id)
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))