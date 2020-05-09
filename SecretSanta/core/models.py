from django.db import models
from django.contrib.auth.models import User
import datetime

# doc user
# https://docs.djangoproject.com/fr/3.0/ref/contrib/auth/


class Secret_santa_group(models.Model):
    group_name = models.CharField(max_length=100)
    master_user = models.ForeignKey(User, models.PROTECT)
    creation_date = models.DateTimeField(default=datetime.datetime.now())

    def __User__(self):
        return self.master_user


class Secret_santa_group_user(models.Model):
    group = models.ForeignKey(Secret_santa_group, models.PROTECT)
    email = models.EmailField()
    # todo on user update update this table too


# FIELDS

class Field(models.Model):
    field_name = models.CharField(max_length=100)


class Field_value(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)


class Field_group(models.Model):
    field = models.ForeignKey(Field, models.PROTECT)
    group = models.ForeignKey(Secret_santa_group, models.PROTECT)


"""
class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(PROTECT=0)
    def __str__(self):
        return self.choice_text


class question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
"""
