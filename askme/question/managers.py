from django.db import models
from django.contrib.auth.models import UserManager
from django.db.models import Sum, Count

class QuestionManager(models.Manager):

    def get_hot(self):
        return self.all().order_by('rating').reverse()

    def get_new(self):
        return self.all().order_by('create_date').reverse()

    def get_by_tag(self, tag_id):
        return self.all().filter(tags__id=tag_id)

    def get_by_user(self, user_id):
        return self.all().filter(author__id=user_id)

    def get_answer_count(self, question_id):
        return self.all().filter(question_id=question_id).count()


class AnswerManager(models.Manager):

    def get_for_answer(self, question_id):
        return self.all().filter(question_id=question_id).order_by('create_date').reverse()

    def get_hot_for_answer(self, question_id):
        return self.all().filter(question_id=question_id).order_by('rating').reverse()

    def get_all_hot(self):
        return self.all().order_by('rating').reverse()


class TagManager(models.Manager):

    def get_by_tag(self, tag_name):
        return self.filter(title=tag_name).first()
        #return self.filter(title=tag_name).first().questions.all().order_by('create_date').reverse()

    def hottest(self):
        return self.annotate(question_count=Count('question')).order_by('-question_count')

class UserManager(UserManager):

    def by_username(self, username):
        return self.all().filter(username=username).first()

    def by_rating(self):
        return self.order_by('-rating')

    def by_first_name(self):
        return self.order_by('first_name')

class LikeManager(models.Manager):
    def liked(self):
        return self.get_queryset().filter(vote__gt=0)

    def disliked(self):
        return self.get_queryset().filter(vote__lt=0)

    def rating(self):
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def questions(self):
        return self.get_queryset().filter(content_type__model='question').order_by('-question__create_date')

    def answers(self):
        return self.get_queryset().filter(content_type__model='answer').order_by('-answer__create_date')