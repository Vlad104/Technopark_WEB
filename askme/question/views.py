# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from question.models import Question, Tag, User, Answer, Like

# Create your views here. ## MY code

def index(request):
    return render(request, 'question/index.html', {
	    	'questions': paginate(request, Question.objects.all()),
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
    	})

def top(request):
    return render(request, 'question/index.html', {
            'questions': paginate(request, Question.objects.get_hot()),
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
        })

def new(request):
    return render(request, 'question/index.html', {
            'questions': paginate(request, Question.objects.get_new()),
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
        })

def user(request, id):
    return render(request, 'question/user.html', {
            'user': get_object_or_404(User, pk=id),
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
    })

def user_questions(request, id):
    return render(request, 'question/index.html', {
            'questions': paginate(request, Question.objects.get_by_user(user_id=id)),
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
    })    

def tag(request, id):
    return render(request, 'question/index.html', {
            'questions': paginate(request, Question.objects.get_by_tag(tag_id=id)),
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
    })

def question(request, id):	
    return render(request, 'question/question.html', {
	    	'question': get_object_or_404(Question, pk=id),
            'answers' : paginate(request, Answer.objects.get_hot_for_answer(id)),
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
   	})

def ask(request):
	return render(request, "question/ask.html", {
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
    })


def login(request):
    return render(request, "question/login.html", {
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
    })

def registration(request):
    return render(request, "question/registration.html", {
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
    })

def paginate(request, objects_list):
    paginator = Paginator(objects_list, 5)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return objects