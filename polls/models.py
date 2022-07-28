import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# 질문과 발행일
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date puvlished')
    # 객체 표시
    def __str__(self):
        return self.question_text
    # 
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# 선택 텍스트와 투표 집계
class Choice(models.Model):
    # 각각의 Choice가 하나의 Question에 관계됨 (1:N)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text