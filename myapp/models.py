from django.db import models

# Create your models here.


class MyFirstTable(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=150)
    age = models.PositiveSmallIntegerField()
    address = models.TextField(max_length=3200000)
    is_activate = models.BooleanField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.email