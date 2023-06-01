from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog, Reviews

# Create your views here.

def home(request:HttpRequest):

    blogs = Blog.objects.all()

    return render(request, 'main_app/home.html', {'blogs' : blogs})

def add_blog(request:HttpRequest):

    if request.method == 'POST':
        new_blog = Blog(title = request.POST['title'], content = request.POST['content'],is_published=request.POST['is_published'], publish_date = request.POST['publish_date'], image = request.FILES['image'] )
        new_blog.save()
        return redirect('main_app:home')

    return render(request, 'main_app/add.html' )

def detail(request:HttpRequest, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        comment = Reviews.objects.filter(blog=blog)
    except:
        return render(request, 'main_app/not_found.html')

    return render(request, 'main_app/detail.html', {'blog' : blog, 'comment' : comment})

def update_blog(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    iso_date = blog.publish_date.isoformat()

    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.is_published = request.POST['is_published']
        blog.publish_date = request.POST['publish_date']
        if 'image' in request.FILES:
            blog.image = request.FILES['image']
        blog.rating = request.POST['rating']
        blog.save()

        return redirect('main_app:detail', blog_id= blog.id)

    return render(request, 'main_app/update.html',{'blog': blog, 'iso_date' : iso_date} )

def delete(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    
    return redirect('main_app:home')

def search(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    blogs = Blog.objects.filter(title__contains=search_phrase,)

    return render(request, "main_app/search.html", {"blogs" : blogs})

def top_blogs(request:HttpRequest):

    blogs = Blog.objects.order_by("-rating")

    return render(request, 'main_app/top_blogs.html', {'blogs' : blogs})

def add_review(request:HttpRequest, blog_id):

    if request.method == "POST":
        blog_object = Blog.objects.get(id=blog_id)
        new_review = Reviews(blog=blog_object, name=request.POST["name"], content=request.POST["content"], rating=request.POST["rating"])
        new_review.save()

    
    return redirect("main_app:detail", blog_id=blog_id)