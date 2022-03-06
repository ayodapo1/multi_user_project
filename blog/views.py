from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def home(request):
    return HttpResponse('<h1>This is the project page</h1>')

def blog_home(request):
    
    all_posts = [
        {
            'author': 'James',
            'title': 'Software Engineering',
            'contents': 'Software engineering is great',
            'date_posted': 'March 5, 2022'
        },

        {
            'author': 'Jackie',
            'title': 'DevOps Engineering on the Rise',
            'contents': 'CI/CD pipeline, a must have skill!',
            'date_posted': 'March 6, 2022'
        }
    ]

    return render(request,"blog/home.html", {"posts": all_posts})

def blog_about(request):
    contents = "Hi, this blog is a platform for several users"
    title = "About"
    return render(request,"blog/about.html", {"about_contents":contents, "title":title})