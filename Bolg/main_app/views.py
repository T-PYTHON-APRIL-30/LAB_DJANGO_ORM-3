from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Blog, Comment


# Create your views here.
def home(request: HttpRequest):
    blog = Blog.objects.filter(is_published = True)

    return render(request, 'main_app/home.html', {"blog" : blog})


def post_page(request: HttpRequest):
    if request.method == "POST":

        new_blog = Blog(
            title = request.POST["title"],
            content = request.POST["content"],
            is_published = request.POST["is_published"]
        )
        new_blog.save()

        return redirect("main_app:home")

    return render(request, 'main_app/post.html')


def detail_page(request: HttpRequest, blog_id):
    try:
        blog = Blog.objects.get(id = blog_id)
        comment = Comment.objects.filter(blog = blog)
    except:
        return render(request, 'main_app/404.html')

    return render(request, 'main_app/detail.html', {"blog" : blog, "comment" : comment})


def update_page(request: HttpRequest, blog_id):
    try:
        blog = Blog.objects.get(id = blog_id)

        if request.method == "POST":
            blog.title = request.POST["title"]
            blog.content = request.POST["content"]
            blog.is_published = request.POST["is_published"]
            blog.save()

            return redirect("main_app:home")
    except:
        return render(request, 'main_app/404.html')

    return render(request, 'main_app/update.html', {"blog" : blog})


def delete_page(request: HttpRequest, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.delete()

    return redirect("main_app:home")


def search_page(request: HttpRequest):
    search_phrase = request.GET.get("search", "")
    blog = Blog.objects.filter(title__contains = search_phrase, is_published = True)

    return render(request, 'main_app/search.html', {"blog" : blog})


def add_comment(request: HttpRequest, blog_id):
    if request.method == "POST":
        blog = Blog.objects.get(id = blog_id)
        new_comment = Comment(
            blog = blog,
            name = request.POST["name"],
            content=request.POST["content"]
        )
        new_comment.save()

    
    return redirect("main_app:detail_page", blog_id = blog_id)


def error_404(request, exception):
    return render(request, 'main_app/404.html')
