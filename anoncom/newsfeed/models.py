import datetime

from django.db import models
from django.utils import timezone


class News(models.Model):
    news_title = models.CharField(max_length=50)
    news_text = models.CharField(max_length=1000)
    news_author = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.news_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    comment_author = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
