from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Posted date - current timezone
    # Otherwise - auto_now_add=True if current exact daytime, not changed
    date_posted = models.DateTimeField(default=timezone.now)
    # One-to-many relationship, when deleted sets the key to null
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Upload Images
    # image = models.ImageField(default='default.png', upload_to='post_images/')

    def __str__(self):
        return self.title

    # Redirect to detail page when post is created
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

        # In case you want to go to home page instead
        # return reverse('blog-home')
    #
    # def save(self, *args, **kwargs):
    #     super(Post, self).save(*args, **kwargs)
    #
    #     # Resizing the profile size
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

