# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from question.models import Question, Tag

# Create your views here. ## MY code

class QuestionList(ListView):
	model = Question
	template_name = 'question/index.html'
	context_object_name = 'questions'
	#paginate_by = 1

class TagList(ListView):
    model = Tag
    template_name = 'question/base.html'
    context_object_name = 'tags'
    #paginate_by = 1

def index(request):
    return render(request, 'question/index.html', {
	    	'question': get_object_or_404(Question, pk=id),
    	})

def question(request, id):	
    return render(request, 'question/question.html', {
	    	'question': get_object_or_404(Question, pk=id),
    	})

def ask(request):
	return render(request, "question/ask.html", {})