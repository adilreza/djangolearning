from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse

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

def manage_data(request):
    if request.method=="GET":
        mydata = Post.objects.all()
        makedictionary = {
            "all_data":mydata
        }
        return render(request, 'manage_data.html', context=makedictionary)

def delete_post(request, id):
    if request.method == "GET":
        Post.objects.filter(id=id).delete()
        mydata = Post.objects.all()
        makedictionary = {
            "all_data": mydata
        }
        return render(request, 'manage_data.html', context=makedictionary)
        #return JsonResponse({"id":id,"message":"Yes your id is received"})

def edit_post(request, id):
    if request.method == "GET":
        mydata = Post.objects.filter(id=id)
        makedictionary = {
            "single_data": mydata
        }
        return render(request, "edit_post.html", context=makedictionary)

def update_post(request):
    if request.method == "POST":
        id = request.POST['id']
        title = request.POST['title']
        description = request.POST['description']

        Post.objects.filter(id=id).update(title=title, description=description)

        mydata = Post.objects.all()
        makedictionary = {
            "all_data": mydata
        }
        return render(request, 'manage_data.html', context=makedictionary)

def manage_data2(request):
    if request.method=="GET":
        mydata = Mydata.objects.all()
        makedictionary = {
            "all_data":mydata
        }
        return render(request, 'manage_data2.html', context=makedictionary)

def delete_post2(request, id):
    if request.method == "GET":
        Mydata.objects.filter(id=id).delete()
        mydata = Mydata.objects.all()
        makedictionary = {
            "all_data": mydata
        }
        return render(request, 'manage_data2.html', context=makedictionary)
        #return JsonResponse({"id":id,"message":"Yes your id is received"})

def edit_post2(request, id):
    if request.method == "GET":
        mydata = Mydata.objects.filter(id=id)
        makedictionary = {
            "single_data": mydata
        }
        return render(request, "edit_post2.html", context=makedictionary)

def update_post2(request):
    if request.method == "POST":
        id = request.POST['id']
        Integer = request.POST['Integer']
        Text = request.POST['Text']
        Character = request.POST['Character']

        Mydata.objects.filter(id=id).update(Integer=Integer, Text=Text, Character=Character)

        mydata = Mydata.objects.all()
        makedictionary = {
            "all_data": mydata
        }
        return render(request, 'manage_data2.html', context=makedictionary)


def response_test(request):
    return HttpResponse("<h1>Hello htppresponse</h1>")

def custome_view(request):
    return HttpResponse("<h1>This is from custom</h1>")