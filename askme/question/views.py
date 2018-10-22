# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here. ## MY code
def index(request):
	questions_list = [
		{"name" : "Как", "id": 1}, 
		{"name" : "перестать", "id": 2},
		{"name" : "делать", "id": 3}, 
		{"name" : "сайты???", "id": 4},
		{"name" : "my fifth question", "id": 5}, 
		{"name" : "my sixth question", "id": 6},
		{"name" : "my seventh question", "id": 7}, 
		{"name" : "my eigth question", "id": 8},
	]
	return render(request, "question/index.html", {
		"questions": questions_list,
	})

def question(request, id):
	return render(request, "question/question.html", {})