from django.urls import path
from . import views

app_name= "main_app"

urlpatterns=[
    path("blog/add/",views.add_blog,name="add_blog"),
    path("",views.read_blog,name="read_blog"),
    path("blog/detail/<post_id>",views.detail_blog,name="detail_blog"),
    path("blog/update/<post_id>", views.update_blog,name="update_blog"),
    path("blog/delete/<post_id>",views.delete_blog,name="delete_blog"),
    path("blog/search/",views.search_page,name="search_page"),
    path("NotFound/",views.not_found,name="not_found"),
    path('blog/detail/add/comment/<post_id>',views.add_comment,name='add_comment'),
    
]
'''path('blog/detail/create/comment/<post_id>',views.create_comment,name="create_comment")'''