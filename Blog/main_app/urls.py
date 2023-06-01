from . import views
from django.urls import path

app_name = 'main_app'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('posts/', views.postsPage, name='postsPage'),
    path('posts/details/<post_id>/',views.detailsPage,name='detailsPage'),
    path('posts/update_post/<post_id>/',views.updatePage,name='updatePage'),
    path('search/',views.searchPage,name='searchPage'),
    path("posts/delete/<post_id>/", views.deletePost, name="deletePost"),
    path("posts/<post_id>/review/add/", views.addReview, name="addReview")

]


