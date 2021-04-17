from django.db import models
from django import forms

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class User(models.Model):
    username = models.CharField(max_length=200)
    groupname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')

class QiangDaItem(models.Model):
    username = models.CharField(max_length=200)
    groupname = models.CharField(max_length=200)
    # password = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)