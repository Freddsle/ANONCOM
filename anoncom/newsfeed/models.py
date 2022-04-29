import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse


class AllPost(models.Model):
    post_title = models.CharField(max_length=50)
    post_text = models.TextField()
    post_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', default=timezone.now, editable=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_absolute_url(self):
        return reverse('newsfeed:detail', args=[str(self.id)])


class Comment(models.Model):
    post_title = models.ForeignKey(AllPost, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    comment_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', default=timezone.now, editable=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text