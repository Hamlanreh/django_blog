from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])


STATUS = (
        ( 0, "Draft" ),
        ( 1, "Publish" )
)


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)      
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])



class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)