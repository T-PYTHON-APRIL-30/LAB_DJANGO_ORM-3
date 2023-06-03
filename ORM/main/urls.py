from django.urls import path
from . import views

app_name="main"
urlpatterns = [
    path("",views.home_page,name="home_page"),
    path('blog/add/',views.add_page,name="add_page"),
    path('blog/detail/<blog_id>/',views.blog_detail,name="blog_detail"),
    path('blog/update/<blog_id>/',views.blog_update,name="blog_update"),
    path('blog/delete/<blog_id>',views.blog_delete,name="blog_delete")
]
