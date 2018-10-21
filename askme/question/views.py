# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here. ## MY code
def index(request):
	questions_list = [
		{"name" : "my first question", "id": 1}, 
		{"name" : "my second question", "id": 2},
	]
	return render(request, "question/index.html", {
		"questions": questions_list,
	})

def question(request, id):
	return render(request, "question/question.html", {})