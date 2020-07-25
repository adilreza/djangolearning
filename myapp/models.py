from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def upload_path(instance, filename):
    return '/'.join(['blog_image', str(instance.blog_image), filename])

def upload_path2(instance, filename):
    return '/'.join(['article_image', str(instance.article_image)])

class MyFirstTable(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=150)
    age = models.PositiveSmallIntegerField()
    address = models.TextField(max_length=3200000)
    is_activate = models.BooleanField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Mydata(models.Model):
    Integer = models.IntegerField()
    Text = models.TextField()
    Character = models.CharField(max_length=200)
    def __str__(self):
        return self.Character


class BlogPost(models.Model):
    blog_image = models.ImageField(blank=True, upload_to=upload_path)
    blog_title = models.CharField(max_length=200)
    blog_description = models.TextField()
    written_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.blog_title

class ArticlePost(models.Model):
    article_image = models.ImageField(blank=False, upload_to=upload_path2)
    article_title = models.CharField(blank=False, max_length=200)
    article_content = models.TextField()
    written_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.article_title

