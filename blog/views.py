from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from .models import Post
# Create your views here.

def home(request):
    return HttpResponse('<h1>This is the project page</h1>')

def blog_home(request):
    # retrieve all posts

    all_posts = Post.published.all()
    #all_posts = Post.objects.all()
    return render(request,"blog/home.html", {"posts": all_posts})

def post_details(request, year, month, day, post_slug):
    # use shortcut to get specific object 

     #status='published',
    post = get_object_or_404(Post, slug=post_slug,
                                    date_published__year=year,
                                    date_published__month=month,
                                    date_published__day=day)
    return render(request, 'blog/details.html', {'post':post})

def blog_about(request):
    contents = "Hi, this blog is a platform for several users"
    title = "About"
    return render(request,"blog/about.html", {"about_contents":contents, "title":title})

