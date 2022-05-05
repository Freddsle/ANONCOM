import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import auth


class AllPost(models.Model):
    post_title = models.CharField(max_length=50)
    post_text = models.TextField()
    post_author = models.ForeignKey(auth.get_user_model(),on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True, editable=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_absolute_url(self):
        return reverse('newsfeed:index', args=[str(self.id)])


class Comment(models.Model):
    post_title = models.ForeignKey(AllPost, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.CharField(max_length=500)
    comment_author = models.ForeignKey(auth.get_user_model(),on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True, editable=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self):
        return reverse('newsfeed:index')
