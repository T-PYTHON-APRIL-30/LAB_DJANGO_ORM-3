from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse,Http404
from .models import Post, Comment

# Create your views here.

def add_post(request:HttpRequest):

    if request.method == "POST":

        new_post = Post(title=request.POST["title"], content=request.POST["content"],
                         is_published=request.POST["is_published"], publish_date=request.POST["publish_date"], image=request.FILES["image"])
        new_post.save()
        return redirect("main_app:index_page")

    return render(request, "main_app/add_post.html")



def index_page(request:HttpRequest):

    posts = Post.objects.all()

    return render(request, "main_app/index.html", {"posts" : posts})


def post_detail(request:HttpRequest, post_id):

    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post)

    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'main_app/post_detail.html', {"post" : post, "comments":comments})


def update_post(request:HttpRequest, post_id):

    post = Post.objects.get(id=post_id)
    iso_date = post.publish_date.isoformat().replace("T", " ").split("+")[0]
    print(iso_date)
    """ - Title : char field
    - Content : text field
    - is_published : boolean field
    - publish_date : datetime field """
    #updating the post
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

    return redirect("main_app:index_page")


def search_page(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    posts = Post.objects.filter(title__contains=search_phrase, is_published=True)

    return render(request, "main_app/search_page.html", {"posts" : posts})

def add_comment(request:HttpRequest, post_id):

    if request.method == "POST":
        post_object = Post.objects.get(id=post_id)
        new_comment = Comment(post=post_object, name=request.POST["name"], content=request.POST["content"])
        new_comment.save()

    
    return redirect("main_app:post_detail", post_id=post_id)