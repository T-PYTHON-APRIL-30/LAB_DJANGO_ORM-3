from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("posts/add/", views.add_post, name="add_post"),
    path("posts/details/<post_id>/", views.post_detail, name="post_detail"),
    path("posts/update/<post_id>/", views.update_post, name="update_post"),
    path("posts/delete/<post_id>/", views.delete_post, name="delete_post"),
    path("posts/search/", views.search_page, name="search_page"),
    path("posts/<post_id>/comment/add/", views.add_comment, name="add_comment")

    ]