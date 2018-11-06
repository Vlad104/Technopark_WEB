# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models

from question.managers import UserManager, TagManager, QuestionManager, AnswerManager, LikeManager

# Create your models here.

class User(AbstractUser):
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/')    
    registration_date = models.DateTimeField(default=timezone.now, verbose_name="Дата решистрации")
    rating = models.IntegerField(default=0, verbose_name="Рейтинг пользователя")

    objects = UserManager()

    def __str__(self):
        return self.username

class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок ярлыка")

    objects = TagManager()

    def __str__(self):
        return self.title  

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")
    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")
    tags = models.ManyToManyField(Tag, blank=True)
    rating = models.IntegerField(default=0, null=False, verbose_name="Рейтинг вопроса")

    objects = QuestionManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)   
    text = models.TextField(verbose_name=u"Полное описание вопроса")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время ответа")
    rating = models.IntegerField(default=0, null=False, verbose_name="Рейтинг ответа")

    objects = AnswerManager()

    def __str__(self):
        return self.text

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    objects = LikeManager()
    
    def __str__(self):
        return self.author + " liked"
