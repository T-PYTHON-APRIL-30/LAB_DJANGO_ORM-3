from django.db import models

# Create your models here.
class Blog(models.Model):
    Title=models.CharField(max_length=2048)
    Content=models.TextField() 
    is_published= models.BooleanField()
    publish_date= models.DateField()
    image=models.ImageField(upload_to="images/",default="images/default.jpg")

class Comment(models.Model):

    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    name= models.CharField(max_length=64)
    contents=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    