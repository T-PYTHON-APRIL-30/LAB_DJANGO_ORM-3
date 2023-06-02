from django.db import models

# Create your models here.

class blog(models.Model,):
    title= models.CharField(max_length=15)
    Content=models.TextField()
    is_published= models.BooleanField()
    publish_date=models.DateField()
    image = models.ImageField(upload_to="images/",default="images/default.jpg")


class Comment(models.Model):
    
    iblog = models.ForeignKey(blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    


