from django.urls import path, include
from .views import user_login, home
urlpatterns = [
    path("login/", user_login),
    path("", home)

]