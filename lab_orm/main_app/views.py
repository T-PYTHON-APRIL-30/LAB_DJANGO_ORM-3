from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Blog,Comment

# Create your views here.
def add_blog(request:HttpRequest):

    if request.method=="POST":
        if "image" in request.FILES:
            new_blog=Blog(Title=request.POST["Title"],Content=request.POST["Content"],is_published=request.POST["is_published"],publish_date=request.POST["publish_date"],image=request.FILES["image"])
        else:
            new_blog=Blog(Title=request.POST["Title"],Content=request.POST["Content"],is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])
            new_blog.save()
            return redirect("main_app:blog_page")

    return render(request,"main_app/add_blog.html")

def blog_page(request:HttpRequest):

    blog=Blog.objects.filter(is_published=True)
    #blog=Blog.objects.all()
    return render(request,"main_app/blog_page.html",{"blog":blog})

def blog_detial(request:HttpRequest,blog_id):

    try:
        blog=Blog.objects.get(id=blog_id)
        comment=Comment.objects.filter(blog=blog)
    except:
        return render(request,"main_app/page_not_found.html")
        
    return render(request,"main_app/blog_detail.html",{'blog':blog,'comments':comment})

def update_blog(request:HttpRequest, blog_id):
    blog=Blog.objects.get(id=blog_id)
    iso_date = blog.publish_date.isoformat()
    if request.method == "POST":
        blog.Title = request.POST["Title"]
        blog.Content = request.POST["Content"]
        blog.is_published = request.POST["is_published"]
        blog.publish_date= request.POST["publish_date"]
        if "image" in request.FILES:
            blog.image= request.FILES["image"]
        blog.save()

        return redirect("main_app:blog_detial",blog_id=blog.id)

    return render(request,"main_app/update_blog.html",{"blog":blog,"iso_date":iso_date})

def delete_blog(request:HttpRequest ,blog_id):
    blog =Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("main_app:blog_page")

def search_page(request:HttpRequest):
    search= request.GET.get("search","")
    blog =Blog.objects.filter(Title__contains=search,is_published=True)

    return render(request,"main_app/search.html",{"blog":blog})

def page_notfound(request:HttpRequest):

    return render(request,"main_app/page_not_found.html")

def add_comment(request:HttpRequest, blog_id):
    
    if request.method=="POST":
        blog_object=Blog.objects.get(id=blog_id)
        newComment=Comment(blog=blog_object, name=request.POST["name"],contents=request.POST["content"])
        newComment.save()

    return redirect("main_app:blog_detial", blog_id=blog_id)

