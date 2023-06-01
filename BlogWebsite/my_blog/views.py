from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponseNotFound
from .models import Blog , Comments
# Create your views here.

def show_page(request:HttpRequest):

    blogs = Blog.objects.all()

    return render(request,"my_blog/show_page.html", {"blogs" : blogs})

def add_page(request:HttpRequest):

    if request.method == "POST":
        
        if "image" in request.FILES:
            new_blog = Blog(title=request.POST["title"], content=request.POST["content"],is_published=request.POST["is_published"], image=request.FILES["image"])
        else:
            new_blog = Blog(title=request.POST["title"], content=request.POST["content"],is_published=request.POST["is_published"])
        new_blog.save()
        return redirect("my_blog:show_page")
    
    return render(request,"my_blog/add_page.html")

def detail_page(request:HttpRequest, blog_id):
    
    try:
        blog = Blog.objects.get( id = blog_id )
        comments = Comments.objects.filter(blog=blog)
    except:
        return render(request, 'my_blog/not_found.html') #Or this call: return HttpResponseNotFound("404")

    return render(request, 'my_blog/detail_page.html', {"blog" : blog, "comments" : comments})


def update_page(request:HttpRequest, blog_id):

    blog = Blog.objects.get( id = blog_id )

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        if "image" in request.FILES:
            blog.image = request.FILES["image"]
        blog.save()
        return redirect("my_blog:detail_page", blog_id = blog.id)

    return render(request, 'my_blog/update_page.html', {"blog" : blog})

def delete_blog(request:HttpRequest,blog_id):

    blog = Blog.objects.get(id = blog_id)
    blog.delete()

    return redirect("my_blog:show_page")



def search_page(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    blogs = Blog.objects.filter(title__contains = search_phrase)

    return render(request, "my_blog/search_page.html", {"blogs" : blogs})

def add_review(request:HttpRequest, blog_id):

    if request.method == "POST":
        blog_object = Blog.objects.get(id=blog_id)
        new_comments = Comments(blog=blog_object, name=request.POST["name"], content=request.POST["content"])
        new_comments.save()

    
    return redirect("my_blog:detail_page", blog_id=blog_id)