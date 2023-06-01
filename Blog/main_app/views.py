from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post ,Comment
from django.utils import timezone
# Create your views here.

def add_blog(request:HttpRequest):

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image=request.FILES['image']
        is_published = bool(request.POST.get('is_published', False))
        publish_date_str = request.POST.get('publish_date')
        if publish_date_str:
            publish_date = timezone.datetime.fromisoformat(publish_date_str)
        else:
            publish_date = timezone.now()
        post = Post.objects.create(title=title, content=content, is_published=is_published, publish_date=publish_date, image=image)
        post.save()
        return redirect('main_app:read_blog')
    else:
        return render(request, "main_app/add_blog.html")


def read_blog(request:HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('publish_date')
    return render(request,"main_app/read_blog.html",{'posts': posts})


def detail_blog(request:HttpRequest, post_id):
    comments=Comment.objects.filter(post=post_id)
    try:
        post= Post.objects.get(id = post_id, is_published=True)
    except Exception:
        return redirect("main_app:not_found")
    return render(request, "main_app/detail.html" ,{'posts':post , "comments" : comments })

def update_blog(request:HttpRequest, post_id):
    post= Post.objects.get(id = post_id)
    iso_date = post.publish_date.isoformat()
    if request.method =="POST":
        post.title = request.POST['title']
        post.content=request.POST['content']
        if "image" in request.FILES:
            post.image=request.FILES['image']
        post.is_published=bool(request.POST.get('is_published', False))
        publish_date_str = request.POST.get('publish_date')
        if publish_date_str:
            post.publish_date = timezone.datetime.fromisoformat(publish_date_str)
        else:
            post.publish_date = timezone.now()
        post.save()
        return redirect('main_app:detail_blog', post_id=post.id)
    
    return render(request, "main_app/update.html",{'posts':post,'iso_date' : iso_date})


def delete_blog(request:HttpRequest, post_id):
    post= Post.objects.get(id= post_id)
    post.delete()
    return redirect("main_app:read_blog")

def search_page(request:HttpRequest):
    if request.method == 'GET':
        search_phrase = request.GET.get("search", "")
        posts = Post.objects.filter(title__icontains= search_phrase,is_published=True )
        return render(request,"main_app/search_page.html",{'posts':posts})
    
def not_found(request:HttpRequest):
    return render(request,"main_app/not_found.html")

def add_comment(request:HttpRequest, post_id):
    if request.method == 'POST':
        post= Post.objects.get(id=post_id)
        new_comment= Comment(post=post,name=request.POST['name'],content=request.POST['content'])
        new_comment.save()
        return redirect('main_app:detail_blog', post_id=post_id)
    return render(request,"main_app/add_comment.html",{"post_id":post_id})
