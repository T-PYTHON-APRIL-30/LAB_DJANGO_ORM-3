from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404
from .models import Post, Review

# Create your views here.

def homePage (request:HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('title')
    return render(request, "main_app/home.html", {"posts" : posts})
    
     
def postsPage(request:HttpRequest):

    if request.method == "POST":
            
        newPost= Post(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], publish_date=request.POST["publish_date"],image=request.FILES["image"] )
        newPost.save()
        return redirect("main_app:homePage")
    
    return render (request,'main_app/post.html') 

def detailsPage(request:HttpRequest,post_id):
    #الأفضل نحطها في تراي واكسبت لأن لو ما حصل الأيدي بيرجع ايرور

    try:
        post = Post.objects.get(id=post_id)
        comments = Review.objects.filter( post= post)

    except:
        return render(request, 'main_app/notFound.html')
    
    return render(request, 'main_app/post_details.html', {"post" : post, "comments": comments})

def updatePage(request:HttpRequest,post_id):

    post = Post.objects.get(id= post_id)
    iso_date = post.publish_date.isoformat()

     #updating the post
    if request.method == "POST":

        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]

        if "image" in request.FILES:
            post.image = request.FILES["image"]

        post.save()

        return redirect("main_app:detailsPage", post_id=post.id)
    
    return render(request,'main_app/update_post.html',{'post': post, 'iso_date':iso_date})

def searchPage(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    posts = Post.objects.filter(title__contains=search_phrase)

    return render(request, "main_app/search.html", {"posts" : posts})

def deletePost(request:HttpRequest, post_id):
    
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect("main_app:homePage")

def addReview(request:HttpRequest, post_id):
     
    if request.method == "POST":

        post_rev = Post.objects.get(id = post_id)

        new_review = Review (post = post_rev, name = request.POST['name'], comment = request.POST['content'])

        new_review.save()
                    
    
    return redirect("main_app:detailsPage", post_id=post_id)
