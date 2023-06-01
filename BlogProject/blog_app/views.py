from django.shortcuts import render ,redirect, get_object_or_404
from django.http import HttpRequest
from .models import Blog , Review

# Create your views here.

def home_page(request:HttpRequest):
    blogs = Blog.objects.filter(is_published="True")

    return render(request,"blog_app/home.html",{"blogs": blogs} )

def add_blog(request:HttpRequest):
    if request.method == "POST":
        #addin a new blog in database
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"], image=request.FILES["image"])
        new_blog.save()
        return redirect("blog_app:home_page")

    return render(request,"blog_app/add_blog.html" )

def read_blog(request:HttpRequest, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id, is_published=True)
        reviews = Review.objects.filter(blog = blog)
        return render(request, 'blog_app/read.html', {'blog': blog , "reviews": reviews})
    except:
        return render(request, 'blog_app/no_blog.html')


def update_blog(request:HttpRequest,blog_id):
    blog =Blog.objects.get(id=blog_id)
    iso_date = blog.publish_date.isoformat()

    #updating
    if request.method == "POST":

        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.publish_date = request.POST["publish_date"]
        if "image" in request.FILES : 
            blog.image = request.FILES["image"]
        blog.save()
        return redirect("blog_app:read_blog", blog_id = blog.id)

    return render(request,"blog_app/update.html",{"blog":blog, "iso_date": iso_date} )

def delete_blog(request:HttpRequest,blog_id):
    blog = Blog.objects.get(id = blog_id)
    blog.delete()

    return redirect("blog_app:home_page")

def no_blog(request:HttpRequest):

    return render(request,"blog_app/no_blog.html")

def search_page(request:HttpRequest):
        
        search_phrase = request.GET.get("search","")
        blogs = Blog.objects.filter(title__contains = search_phrase)
        return render(request, "blog_app/search.html", {"blogs" : blogs})

def add_review(request:HttpRequest, blog_id):

    if request.method == "POST":
        blog_object = Blog.objects.get(id=blog_id)
        new_review = Review(blog = blog_object, name = request.POST["name"], content = request.POST["content"])
        new_review.save()
    return redirect("blog_app:read_blog", blog_id = blog_id)