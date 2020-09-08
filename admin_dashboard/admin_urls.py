from django.urls import path, include
from .views import user_login, home, register
urlpatterns = [
    path("login/", user_login),
    path("register/", register),
    path("", home)

]