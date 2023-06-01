from django.db import models

# Create your models here.
class Post(models.Model):

    title= models.CharField(max_length=2000)
    content= models.TextField()
    image=models.ImageField(upload_to="images/",default="images/defult.jpg")
    is_published = models.BooleanField(default=False)
    publish_date = models.DateTimeField()

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    content=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    