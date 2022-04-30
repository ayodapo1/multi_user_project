from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.blog_home, name="blog_home"),
    path('about/', views.blog_about, name="blog_about"),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', 
          views.post_details, name="post_details"),
]
