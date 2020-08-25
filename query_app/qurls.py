from django.urls import path, include
from .views import hello_world, start_with_f, limit_with, list_filtering
urlpatterns = [
    path("",hello_world),
    path("start/<slug:start_with>", start_with_f),
    path('limit/<int:limit_from>/<int:limit_to>',limit_with),
    path('list_filtering/',list_filtering)

]