from django.urls import path, include

from .views import custome_view
from .views import make_user, make_login, logout_here
urlpatterns = [
    path("path1/",custome_view),
    path("signup/",make_user),
    path("login/", make_login),
    path("logout", logout_here),

]