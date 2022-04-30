from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# create a manager for retrieving published posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self)\
            .get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    # post attributes or fields
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique_for_date='date_published')
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES, 
                                default='draft')
    
    # order according to most recent post
    class Meta:
        ordering = ('-date_published',)
    # string representation of post
    def __str__(self):
        return self.title

    # methods for getting absolute url
    # reverse() allows you to build a url
    def get_absolute_url(self):
        return reverse('blog:post_details',
                       args=[self.date_published.year,
                             self.date_published.month,
                             self.date_published.day, 
                             self.slug])

    # define managers 
    objects = models.Manager() # default manager
    published = PublishedManager() #custom manager


    








    