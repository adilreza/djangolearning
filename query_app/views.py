from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
from .models import Entry, Author, Blog

def hello_world(request):
    return JsonResponse({"msg":"Hello I am from hello world"})


def start_with_f(request, start_with):
    data = Blog.objects.filter(tagline__startswith=start_with).values()
    data_list = list(data)
    return JsonResponse({"rcv":data_list})


def limit_with(request, limit_from, limit_to):
    data = Author.objects.order_by("name")[limit_from:limit_to].values()
    data_list = list(data)

    return JsonResponse({"Result": data_list})

def list_filtering(request, ):
    data = Entry.objects.filter(pk__in=[5,3,4,8,9])
    print(data)
    return JsonResponse({"hello":"hello"})


