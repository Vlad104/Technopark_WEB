# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponseForbidden as Http403, HttpResponse
from django.contrib.auth.decorators import login_required
import json
from question.models import Question, Tag, User, Answer, Like
from question.forms import UserRegistrationForm, UserLoginForm, UserSettingsForm, AskForm, AnswerForm

def index(request):
    return render(request, 'question/index.html', {
	    	'questions': paginate(request, Question.objects.all()),
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
            'page_objects' : paginate(request, Question.objects.all()),
    	})

def top(request):
    return render(request, 'question/index.html', {
            'questions': paginate(request, Question.objects.get_hot()),
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
            'page_objects' : paginate(request, Question.objects.all()),
        })

def new(request):
    return render(request, 'question/index.html', {
            'questions': paginate(request, Question.objects.get_new()),
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
            'page_objects' : paginate(request, Question.objects.all()),
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
            'page_objects' : paginate(request, Question.objects.get_by_user(user_id=id)),
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
            'page_objects' : paginate(request, Answer.objects.get_hot_for_answer(id)),
   	})


#@login_required(login_url='/signin/')
def new_answer(request, question_id):
    if Question.objects.filter(id=question_id).exists():
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                answeredQuestion = Question.objects.get_by_id(question_id)[0]
                answer = Answer.objects.create(author=request.user,
                                date=timezone.now(),
                                text=form.cleaned_data['text'],
                                question_id=answeredQuestion.id)
                answer.save()
                return redirect('/question/{}/#{}'.format(question_id, answer.id))
        else:
            form = AnswerForm()
        return render(request, 'question/new_answer.html', {'form': form})
    else:
        raise Http404

@login_required(login_url='/login/')
def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            ques = Question.objects.create(author=request.user,
                            date=timezone.now(),
                            is_active=True,
                            title=form.cleaned_data['title'],
                            text=form.cleaned_data['text'])
            ques.save()

            for tagTitle in form.cleaned_data['tags'].split():
                tag = Tag.objects.get_or_create(name=tagTitle)[0]
                ques.tags.add(tag)
                ques.save()
            return question(request, ques.id)
    else:
        form = AskForm()
    return render(request, 'question/ask.html', {
            'form': form,
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
        })


def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next') if request.GET.get('next') != '' else '/')
    else:
        form = UserLoginForm()
        logout(request)
    return render(request, 'question/login.html', {
            'form': form,
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
        })

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
        logout(request)
    return render(request, 'question/registration.html', {
            'form': form,
            'tags' : paginate(request, Tag.objects.hottest()),
            'users' : paginate(request, User.objects.by_rating()),
        })

def signout(request):
    if not request.user.is_authenticated:
        raise Http404
    logout(request)
    return redirect(request.GET['from'])


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