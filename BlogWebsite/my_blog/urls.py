from django.urls import path
from . import views

app_name = "my_blog"

urlpatterns = [ 
    path("", views.show_page, name="show_page"),
    path("add/blog/",views.add_page,name="add_page"),
    path("detail/blog/<blog_id>/", views.detail_page, name="detail_page"),
    path("update/blog/<blog_id>/", views.update_page, name="update_page"),
    path("delete/blog/<blog_id>/", views.delete_blog, name="delete_blog"),
    path("review/add/blog/<blog_id>/", views.add_review, name="add_review"),
    path("search/blog/", views.search_page, name="search_page"),
]