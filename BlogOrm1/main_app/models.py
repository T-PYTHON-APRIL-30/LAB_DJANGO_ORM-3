from django.db import models
from django.utils import timezone


class Post(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=2048)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    publish_date = models.DateField()
    images = models.ImageField(upload_to="images/",default="images/default.jpeg")


class Comment(models.Model):
    objects = None
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

