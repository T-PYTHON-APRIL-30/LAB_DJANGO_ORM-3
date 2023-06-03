from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from .models import Blog,Review
# Create your views here.
def home_page(request:HttpRequest):

    #for searching
    if request.GET.fromkeys("search"):

        search_phrase = request.GET.get("search", "")
        blogs=Blog.objects.filter(title__contains=search_phrase,)

        return render(request,"main/home_page.html",{"blogs" : blogs ,"search_phrase":search_phrase})

    blogs =Blog.objects.all()
    return render(request,"main/home_page.html",{"blogs" : blogs})



def add_page(request:HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], contant=request.POST["contant"],  is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])
        new_blog.save()

    return render(request,"main/add_page.html")



def blog_detail(request:HttpRequest,blog_id):
    try:

        blog=Blog.objects.get(id=blog_id)

    except Exception:

        return HttpResponseNotFound('<h1>page not found!</h1>')

    return render(request,"main/blog_detail.html",{"blog":blog})



def blog_update(request:HttpRequest,blog_id):

    blog=Blog.objects.get(id=blog_id)
    iso_date =blog.publish_date.isoformat()
    if request.method=='POST':
        blog.title=request.POST["title"]
        blog.contant=request.POST["contant"]
        blog.is_published=request.POST["is_published"]
        blog.publish_date=request.POST["publish_date"]
        blog.save()
        return redirect("main:blog_detail",blog_id=blog.id)
    return render(request,'main/blog_update.html',{"iblog":blog,"iso_date":iso_date})




def blog_delete(request:HttpRequest,blog_id):
    blog=Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect("main:home_page")


def add_review(request:HttpRequest, blog_id):

    if request.method == "POST":
        blog_object = Blog.objects.get(id=blog_id)
        new_review = Review(blog=blog_object, name=request.POST["name"], contant=request.POST["contant"])
        new_review.save()

    
    return redirect("main:blog_detail", blog_id=blog_id)
