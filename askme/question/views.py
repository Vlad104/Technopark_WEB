# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from question.models import Question, Tag, User, Answer, Like, Profile

# Create your views here. ## MY code

class QuestionList(ListView):
	model = Question
	template_name = 'question/index.html'
	context_object_name = 'questions'
	paginate_by = 5

class TagList(ListView):
    model = Tag
    #queryset = Tag.objects.all()
    template_name = 'question/index.html'
    context_object_name = 'tags'
    paginate_by = 10

#def index(request):
#    return render(request, 'question/index.html', {
#	    	'question': get_object_or_404(Question, pk=id),
#            'tags' : Tag.objects.all(),
#    	})

#def tags(request):
#    return render(request, 'question/index.html', {
#            'tags': Question.objects.all(),
#    })    

def question(request, id):	
    return render(request, 'question/question.html', {
	    	'question': get_object_or_404(Question, pk=id),
   	})

def ask(request):
	return render(request, "question/ask.html", {})

def login(request):
    return render(request, "question/login.html", {})

def registration(request):
    return render(request, "question/registration.html", {})

def settings(request):
    return render(request, "question/settings.html", {})

#def paginate(objects_list, request):
    # do smth with Paginator, etc…
#    return objects_page, paginator