from django.urls import path
from . import views


app_name = "new_movie"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("add/", views.add_page , name="add_page"),
    path("view/", views.view_page , name="view_page"),
    path("details/<movie_id>/", views.detail_page, name="detail_page"),
    path("update/<movie_id>/", views.update_page, name="update_page"),
    path("delete/<movie_id>/", views.delete_page, name="delete_page"),
    path("search/", views.search_page, name="search_page"),
    path("not_found/", views.notfound, name="not_found"),
    path("details/<movie_id>/reviews/", views.review, name="review")

]