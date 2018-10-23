# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from question.models import Question

# Create your views here. ## MY code
def index(request):
	questions_list = [
		{"name" : "Как", "id": 1}, 
		{"name" : "перестать", "id": 2},
		{"name" : "делать", "id": 3}, 
		{"name" : "сайты???", "id": 4},
		{"name" : "ааааааааааа", "id": 5}, 
		{"name" : "ааааааааааа", "id": 6},
	]
	tags_list = [	
		{"name" : "Антоха", "id": 1}, 
		{"name" : "пауки", "id": 2},
		{"name" : "html", "id": 3}, 
		{"name" : "картоха", "id": 4},
	]
	return render(request, "question/index.html", {
		"questions": questions_list,
		"tags": tags_list,
	})

def question(request, question_id):
    return render(request, 'question/question.html', {
	    	'question': get_object_or_404(Question, pk=question_id)
    	})

def question_old(request, id):	
	answer_list = [
		{"name" : "Пиши по русски!!!!", "id": 1}, 
		{"name" : "Загугли", "id": 2},
		{"name" : "не гугли, подумой", "id": 3}, 
	]

	tags_list = [	
		{"name" : "Антоха", "id": 1}, 
		{"name" : "пауки", "id": 2},
		{"name" : "html", "id": 3}, 
		{"name" : "картоха", "id": 4},
	]
	return render(request, "question/question.html", {
			"answers": answer_list,
			"tags": tags_list,
		})

def add_question(request):
	tags_list = [	
		{"name" : "Антоха", "id": 1}, 
		{"name" : "пауки", "id": 2},
		{"name" : "html", "id": 3}, 
		{"name" : "картоха", "id": 4},
	]
	return render(request, "question/add_question.html", {
			"tags": tags_list,
		})