from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseNotFound, Http404
from .models import Post , Comment


def add_post(request: HttpRequest):
    if request.method == "POST":
        # addin a new post in database
        new_post = Post(title=request.POST["title"], description=request.POST["description"],
                        publish_date=request.POST["publish_date"],
                        is_published=request.POST["is_published"],images=request.FILES['image'])
        new_post.save()
        return redirect("main_app:index_page")

    return render(request, "main_app/add_post.html")


def index_page(request: HttpRequest):
    posts = Post.objects.all()

    return render(request, "main_app/index.html", {"posts": posts})



def post_detail(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id, is_published=True)
        comments = Comment.objects.filter(post=post)
        return render(request, 'main_app/post_detail.html', {"post": post , "comments":comments})
    except Http404:
        return HttpResponseNotFound('Page not found')

def update_post(request: HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    iso_date = post.publish_date.isoformat()

    # updating the post
    if request.method == "POST":
        post.title = request.POST["title"]
        post.description = request.POST["description"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        if "image" in request.FILES:
            post.images = request.FILES['image']
        post.save()

        return redirect("main_app:post_detail", post_id=post.id)

    return render(request, 'main_app/update_post.html', {"post": post, "iso_date": iso_date})


def delete_post(request: HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect("main_app:index_page")


def search_page(request: HttpRequest):
    search_phrase = request.GET.get("search", "")
    posts = Post.objects.filter(title__contains=search_phrase, is_published='True')

    return render(request, "main_app/search_page.html", {"posts": posts})


def add_review(request: HttpRequest, post_id):
    if request.method == "POST":
        post_object = Post.objects.get(id=post_id)
        new_review = Comment(post=post_object, name=request.POST["name"], content=request.POST["content"])
        new_review.save()

    return redirect("main_app:post_detail", post_id=post_id)