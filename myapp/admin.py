from django.contrib import admin


# imported all models

from .models import MyFirstTable
from .models import Post, Mydata, BlogPost
# Register your models here.


admin.site.register(MyFirstTable)
admin.site.register(Post)
admin.site.register(Mydata)
admin.site.register(BlogPost)