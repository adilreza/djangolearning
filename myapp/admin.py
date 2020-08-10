from django.contrib import admin


# imported all models

from .models import MyFirstTable
from .models import Post, Mydata, BlogPost, MyAjaxTest, CharlotteAjaxTable
from .models import AdvancedDataType
# Register your models here.


admin.site.register(MyFirstTable)
admin.site.register(Post)
admin.site.register(Mydata)
admin.site.register(BlogPost)
admin.site.register(MyAjaxTest)
admin.site.register(CharlotteAjaxTable)
admin.site.register(AdvancedDataType)


admin.site.site_header = "Django Learning"
admin.site.site_title = "Welcome to admin dashboard"
admin.site.index_title = "Learning"