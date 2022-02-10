from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_home, name="blog_home"),
    path('about/', views.blog_about, name="blog_about")
]
