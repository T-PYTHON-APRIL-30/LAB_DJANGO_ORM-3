from django.urls import path
from . import views

app_name = 'main_app'


urlpatterns = [
    path('', views.base_page, name='base_page'),
    path("search/", views.search_page, name="search_page"),
    path('add_post', views.add_post, name='add_post'),
    path('post_detail/<post_id>', views.post_detail, name='post_detail'),
    path('post_detail/update_post/<post_id>', views.update_post, name='update_post'),
    path("post_detail/delete/<post_id>/", views.delete_post, name="delete_post"),
    path("post_detail/<post_id>/review/", views.add_review, name="add_review")

    
 
]