"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import index_file
from myapp.views import adil_file, charlotte_file, newpage
from myapp.views import about, contact, my_form, my_form2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index_file),
    path('adil/', adil_file),
    path('newpage/', newpage),
    path('about/', about),
    path('contact/', contact),
    path('post/', my_form),
    path('', charlotte_file),
    path('form2/', my_form2),

]
