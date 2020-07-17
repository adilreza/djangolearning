from django.contrib import admin


# imported all models

from .models import MyFirstTable
from .models import Post
# Register your models here.


admin.site.register(MyFirstTable)
admin.site.register(Post)