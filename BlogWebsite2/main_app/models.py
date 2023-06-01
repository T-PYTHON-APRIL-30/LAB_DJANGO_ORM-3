from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    publish_date = models.DateTimeField()
    

class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

