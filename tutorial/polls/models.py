from datetime import timedelta
from django.db import models
from django.utils import timezone


class Question(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'설문조사 ({self.title})'

    def is_recently(self):

        return bool(self.published_date) and \
               (timezone.now() - self.published_date <= timedelta(days=7))


class Choice(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} ({self.question.title})'
