from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import movie, Reviews

# Create your views here.

def home_page(request:HttpRequest):

    movies = movie.objects.filter(is_published = True)

    return render(request, "new_movie/home.html", {"movies": movies})

def add_page(request:HttpRequest):
    if request.method == "POST":
        
        new_movie = movie(title=request.POST["title"],
                        content=request.POST["content"],
                         is_published=request.POST["is_published"],
                         publish_date=request.POST["publish_date"])
        if "image" in request.FILES:
            new_movie.image=request.FILES["image"]
        new_movie.save()
        return redirect("new_movie:view_page")

    return render(request, "new_movie/add_page.html")


def view_page(request:HttpRequest):
     
    movies = movie.objects.all()

    return render(request, "new_movie/view_page.html", {"movies": movies})


def detail_page(request:HttpRequest, movie_id):

    movie_d = movie.objects.get(id=movie_id)
    comments = Reviews.objects.filter(movie=movie_d)

    return render(request,"new_movie/details.html", {"movie_d" : movie_d, "comments": comments})


def update_page(request:HttpRequest, movie_id):

    movie_u = movie.objects.get(id=movie_id)
    iso_date = movie_u.publish_date.isoformat()

    if request.method == "POST":
        movie_u.title = request.POST["title"]
        movie_u.content = request.POST["content"]
        movie_u.is_published = request.POST["is_published"]
        movie_u.publish_date = request.POST["publish_date"]
        if "image" in request.FILES:
            movie_u.image=request.FILES["image"]
        movie_u.save()
        return redirect("new_movie:view_page")
    
    return render(request, ("new_movie/update.html"), {"movie_u":movie_u, "iso_date":iso_date})

def delete_page(request:HttpRequest, movie_id):

    movie_de = movie.objects.get(id=movie_id)
    movie_de.delete()

    return redirect("new_movie:view_page")


def search_page(request:HttpRequest):
    
    search_phrase = request.GET.get("search","")
    movie_s = movie.objects.filter(title__contains = search_phrase)
    if len(movie_s) != 0:
        return render(request, "new_movie/search.html", {"movie_s":movie_s})
    else:
        return redirect("new_movie:not_found")
    

def notfound(request:HttpRequest):

    return render(request,"new_movie/not_found.html")


def review(request:HttpRequest, movie_id):

    if request.method == "POST":
        movie_rev = movie.objects.get(id=movie_id)
        movie_com = Reviews(movie=movie_rev, name= request.POST["name"], comment= request.POST["comment"])
        movie_com.save()

    return redirect("new_movie:detail_page", movie_id=movie_id)
