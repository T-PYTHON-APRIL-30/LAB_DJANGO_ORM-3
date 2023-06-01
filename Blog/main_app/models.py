from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)