from django.urls import path, include

from .views import custome_view
urlpatterns = [
    path("path1/",custome_view)
]