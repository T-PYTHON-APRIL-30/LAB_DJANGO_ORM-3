from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import blog,comment
from django.db.models import Q

# Create your views here.

def index_page(request:HttpRequest):
    blogs = blog.objects.all()
    return render(request, "solution/index.html", {"blogs":blogs})

def read_blog(request:HttpRequest, blog_id):
    Blog = blog.objects.get(id = blog_id)
    Comments = comment.objects.filter(Blog=Blog) 
    return render(request, 'solution/blog_read.html', {"Blog":Blog, "Comments": Comments})

def add_comment(request:HttpRequest, blog_id):
    if request.method == "POST":
        Blog1 = blog.objects.get(id = blog_id)
        Comment = comment(Blog = Blog1, name = request.POST["name"], content = request.POST["content"])
        Comment.save()
    return redirect("solution:read_blog", blog_id = blog_id)


def add_blog(request:HttpRequest):

    if request.method == "POST":
        new_blog = blog(title=request.POST["title"], context=request.POST["context"], is_published=request.POST["is_published"], publish_date = request.POST["publish_date"], image = request.FILES["image"] )
        new_blog.save()
        return redirect("solution:index_page")

    return render(request, "solution/blog_add.html")

def blog_update(request:HttpRequest, blog_id):
    Blog = blog.objects.get(id = blog_id)
    iso_date = Blog.publish_date.isoformat()
    if request.method == "POST":
        Blog.title = request.POST["title"]
        Blog.context = request.POST["context"]
        Blog.is_published = request.POST["is_published"]
        Blog.publish_date = request.POST["publish_date"]
        if "image" in request.FILES:
            Blog.image = request.FILES["image"]
            
        Blog.save()
        return redirect("solution:read_blog", blog_id = Blog.id)
    
    return render(request, "solution/blog_update.html", {"Blog":Blog, "iso_date":iso_date})

def blog_delete(request:HttpRequest, blog_id):
    Blog = blog.objects.get(id = blog_id)
    Blog.delete()
    return redirect("solution:index_page")

def blog_search(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    blogs = blog.objects.filter(title__contains=search_phrase,)
    return render(request, "solution/blog_search.html", {"blogs" : blogs})
