from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.

# 질문과 발행일
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date puvlished')

# 선택 텍스트와 투표 집계
class Choice(models.Model):
    # 각각의 Choice가 하나의 Question에 관계됨 (1:N)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)