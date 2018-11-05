from django.db import models
from django.contrib.auth.models import UserManager
from django.db.models import Sum, Count

class QuestionManager(models.Manager):

    def get_hot(self):
        return self.all().order_by('rating').reverse()

    def get_new(self):
        return self.all().order_by('create_date').reverse()

    def get_by_id(self, question_id):
        return self.all().filter(id=question_id)

    def get_by_tag(self, question_id, tag):
        #return self.all().filter(tags__exact=tag)
        return self.all()

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
    def likes(self):
        return 0