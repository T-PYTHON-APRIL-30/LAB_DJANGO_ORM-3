from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/", default="images/default.png")

class Review(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
