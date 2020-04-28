from django.db import models
from django.contrib.auth.models import User
import datetime

# doc user
# https://docs.djangoproject.com/fr/3.0/ref/contrib/auth/


class group(models.Model):
    id = models.AutoField(primary_key=True)
    master_user = models.ForeignKey(User, models.PROTECT)
    creation_date = models.DateTimeField(datetime.datetime.now())

    def __User__(self):
        # not todo here this is disgusting
        return self.master_user


class group_user(models.Model):
    group = models.ForeignKey(group, models.PROTECT)
    user = models.ForeignKey(User, models.PROTECT)


# FIELDS

class field(models.Model):
    id = models.AutoField(primary_key=True)
    field_name = models.CharField(max_length=100)


class field_value(models.Model):
    id = models.AutoField(primary_key=True)
    field = models.ForeignKey(field, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)


class field_group(models.Model):
    field = models.ForeignKey(field, models.PROTECT)
    group = models.ForeignKey(group, models.PROTECT)


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
