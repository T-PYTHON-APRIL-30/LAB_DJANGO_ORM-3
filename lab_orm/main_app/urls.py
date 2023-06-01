from django.urls import path
from . import views

app_name= "main_app"

urlpatterns= [
    path("",views.blog_page,name="blog_page"),
    path("blog/add",views.add_blog,name="add_blog"),
    path("blog/detail/<blog_id>",views.blog_detial,name="blog_detial"),
    path("blog/update/<blog_id>",views.update_blog,name="update_blog"),
    path("blog/delete/<blog_id>/", views.delete_blog, name="delete_blog"),
    path("blog/search",views.search_page,name="search_page"),
    path("blog/notFound",views.page_notfound,name="page_notfound"),
    path("blog/<blog_id>/comment",views.add_comment,name="add_comment")

]