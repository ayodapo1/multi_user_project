from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def home(request):
    return HttpResponse("<h1> This is the project home page </h1>")

def blog_home(request):
    return HttpResponse("<h1> This is the blog's home page </h1>")

def blog_about(request):
    return HttpResponse("<h1> This is the blog's about page </h1>")