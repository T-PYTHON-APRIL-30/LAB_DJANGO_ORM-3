from django.db import models

# Create your models here.


class movie(models.Model):

        title = models.CharField(max_length=200)
        content = models.TextField()
        is_published = models.BooleanField()
        publish_date = models.DateTimeField()
        image = models.ImageField(upload_to="images", default="images/default.jpg")

class Reviews(models.Model):
        movie = models.ForeignKey(movie, on_delete=models.CASCADE)
        name = models.CharField(max_length=150)
        comment = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
