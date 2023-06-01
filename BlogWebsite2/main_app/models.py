from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    publish_date = models.DateTimeField()
    