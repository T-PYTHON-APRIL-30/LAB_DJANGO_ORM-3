from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 512)
    content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)

    name = models.CharField(max_length = 512)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
