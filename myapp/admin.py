from django.contrib import admin


# imported all models

from .models import MyFirstTable

# Register your models here.


admin.site.register(MyFirstTable)