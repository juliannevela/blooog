from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# Blog post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title

# Author model
class Author(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  website = models.URLField()

# Category model
class Category(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  date_updated = models.DateTimeField(auto_now=True, null=True)

# Comment model
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  content = models.TextField()
  date_posted = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

# Profile model
class Profile(models.Model):
  user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
  bio = models.TextField()
