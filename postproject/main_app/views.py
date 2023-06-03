from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post, Review
# Create your views here.

def base_page(request:HttpRequest ):
    view_post = Post.objects.all()
    return render(request, "main_app/base.html", {"view_post" : view_post})


def add_post(request:HttpRequest):
    if request.method == "POST":
            new_post = Post(name=request.POST["name"], title=request.POST["title"], description=request.POST["description"], date=request.POST["date"], img = request.FILES["img"])
            new_post.save()
            return redirect("main_app:base_page")
    return render (request, "main_app/add_post.html")


def post_detail(request:HttpRequest, post_id):
     post_detail1 = Post.objects.get(id = post_id)
     comments = Review.objects.filter(post=post_detail1)
     return render (request,"main_app/post.html",{"post_detail1" : post_detail1, "comments" : comments})


def update_post(request:HttpRequest,post_id):
    update_detail1 = Post.objects.get(id = post_id)
    iso_date = update_detail1.date.isoformat()
    if request.method == "POST":
            update_detail1.name =request.POST["name"]
            update_detail1.title=request.POST["title"]
            update_detail1.description = request.POST["description"]
            update_detail1.date = request.POST["date"]
            update_detail1.save()
            return redirect("main_app:post_detail", post_id = update_detail1.id)
    return render (request,"main_app/update_post.html",{"update_detail1" : update_detail1,"iso_date" : iso_date})


def delete_post(request:HttpRequest, post_id):
    delete_detail1 = Post.objects.get(id = post_id)
    delete_detail1.delete()
    return redirect("main_app:base_page")



def search_page(request:HttpRequest):
    
    search_phrase = request.GET.get("search", "")
    posts = Post.objects.filter(title__contains=search_phrase)

    return render(request, "main_app/search_page.html", {"posts" : posts})


def add_review(request:HttpRequest, post_id):

    if request.method == "POST":
        post_object = Post.objects.get(id=post_id)
        new_review = Review(post=post_object, name=request.POST["name"], content=request.POST["content"])
        new_review.save()

    
    return redirect("main_app:post_detail", post_id=post_id)from django.shortcuts import render

# Create your views here.
