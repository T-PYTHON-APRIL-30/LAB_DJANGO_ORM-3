from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField(default="Post")
    date = models.DateField()
    img = models.ImageField(upload_to="img/",default="img/bears.jpg")

class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
