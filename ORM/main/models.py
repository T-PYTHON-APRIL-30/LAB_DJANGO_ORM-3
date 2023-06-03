from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=2064)
    contant = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()

class Review(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    contant = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
