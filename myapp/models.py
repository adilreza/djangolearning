from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import pre_save, post_save


# Create your models here.


def upload_path(instance, filename):
    return '/'.join(['blog_image', str(instance.blog_image), filename])


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


class MyAjaxTest(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.name


class CharlotteAjaxTable(models.Model):
    name = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class AdvancedDataType(models.Model):
    name = models.CharField(max_length=30)
    json_data = JSONField()

    def __str__(self):
        return self.name

class DjangoSignal(models.Model):
    title = models.CharField(max_length=250)
    details = models.CharField(blank=True, null=True, max_length=250)

    def __str__(self):
        return self.title


def save_post(sender, instance, **kwargs):
    print("this function is called ")


post_save.connect(save_post, sender=DjangoSignal)
