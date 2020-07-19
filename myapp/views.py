from django.shortcuts import render

# import model
from .models import  Post, Mydata

# Create your views here.

def index_file(request):
    return render(request, 'index.html')

def adil_file(request):
    return render(request, 'adil.html')

def charlotte_file(request):
    return render(request, 'charlotte.html')

def newpage(request):
    return render(request, 'newpage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def my_form(request):
    if request.method=="GET":
        return render(request, 'firstform.html')
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        sql = Post(title=title, description=description)

        sql.save()
        return render(request, 'firstform.html')


def my_form2(request):
    if request.method=="GET":
        return render(request, 'secondform.html')
    if request.method == "POST":
        integer = request.POST['Integer']
        print(integer)
        text= request.POST['Text']
        character= request.POST['Character']

        sql = Mydata(Integer=integer, Text=text, Character=character)

        sql.save()
        return render(request, 'secondform.html')