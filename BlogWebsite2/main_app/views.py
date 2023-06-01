from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def add_blog(request:HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"], image=request.FILES["image"])
        new_post.save()
        return redirect("main_app:index.html")
    return render(request, "main_app/add_blog.html")


def index_page(request:HttpRequest):

    
    posts = Post.objects.filter(is_published="True")

    return render(request, "main_app/index.html", {"posts" : posts}) 


def not_found(request:HttpRequest):

    return render(request,"main_app/not_found.html")


def post_detail(request:HttpRequest, post_id):
    try:
        post = Post.objects.get(id= post_id)
    except:
        return render(request, 'main_app/not_found.html')

    return render(request, "main_app/post_detail.html", {"post" : post})


def update_post(request:HttpRequest, post_id):

    post = Post.objects.get(id=post_id)
    iso_date = post.publish_date.isoformat()

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.is_published = request.POST["is_published"]
        post.publish_date = request.POST["publish_date"]
        
        if "image" in request.FILES:
            post.image = request.FILES["image"]
        post.save()



        return redirect("main_app:post_detail", post_id=post.id)

    return render(request, 'main_app/update_post.html', {"post" : post, "iso_date" : iso_date})



def delete_post(request:HttpRequest, post_id):
    
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("main_app:delete_done")



def delete(request:HttpRequest):

    return render(request,"main_app/index.html")


def search_page(request:HttpRequest):

    search_phrase = request.GET.get("search", "")
    posts = Post.objects.filter(title__contains=search_phrase,)
    
    return render(request, "main_app/search_page.html", {"posts" : posts})




