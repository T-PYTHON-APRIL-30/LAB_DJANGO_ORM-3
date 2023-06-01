from django.db import models
from datetime import date

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=2048)
    context = models.TextField()
    image = models.ImageField(upload_to="images/",default="images/img1.jpg")
    is_published = models.BooleanField(default=True)
    publish_date = models.DateField()


class comment(models.Model):
    Blog = models.ForeignKey(blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)