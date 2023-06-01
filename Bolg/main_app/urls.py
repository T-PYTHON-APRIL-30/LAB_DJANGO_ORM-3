from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('post/', views.post_page, name = 'post_page'),
    path('post/detail/<blog_id>', views.detail_page, name = 'detail_page'),
    path('post/update/<blog_id>', views.update_page, name = 'update_page'),
    path('post/delete/<blog_id>', views.delete_page, name = 'delete_page'),
    path('post/search/', views.search_page, name = 'search_page'),
    path('post/update/<blog_id>/comment/', views.add_comment, name='add_comment')
]
