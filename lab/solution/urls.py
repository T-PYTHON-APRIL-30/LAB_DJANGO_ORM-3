from django.urls import path
from . import views

app_name = "solution"

urlpatterns = [
path("", views.index_page, name="index_page"),
path("blog/read/<blog_id>/", views.read_blog, name="read_blog"),
path("blog/add/", views.add_blog, name="add_blog"),
path("blog/search/", views.blog_search, name="search_blog"),
path("blog/update/<blog_id>/", views.blog_update, name="update_blog"),
path("blog/delete/<blog_id>/", views.blog_delete, name="delete_blog"),
path("blog/<blog_id>/comment/add/", views.add_comment, name="comment_add")


]