from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
# import model
from .models import  Post, Mydata, BlogPost, MyAjaxTest
# Create your views here.
import json

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
    if request.user.is_authenticated:
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

def make_user(request):
    if request.method=="GET":
        return render(request, 'signup.html')
    if request.method=="POST":

        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        usr = User.objects.create_user(username=username, email=email, password=password)
        usr.save()
        return JsonResponse({"message":"Successfully create a new user"})


def make_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            request.session['my_auth_user']=username
            return JsonResponse({"message":"Yooo!! yes you are our valid user, Welcome"})
        else:
            return JsonResponse({"message":"Noo!! you are not our valid user"})


def logout_here(request):
    logout(request)
    request.session['my_auth_user'] = ''
    return JsonResponse({"message":"You have been  successfully log out"})

def blogpost(request):
    if request.method == "GET":
        return render(request, 'blogpost.html')

    if request.method == "POST":
        usr = request.session.get('my_auth_user')

        if usr:
            user = User.objects.get(username=request.session['my_auth_user'])
            blog_title = request.POST['blog_title']
            blog_description = request.POST['blog_description']
            blog_image = request.FILES['blog_image']
            # print(blog_description)
            sql = BlogPost(blog_title=blog_title, blog_image=blog_image, blog_description=blog_description,
                           written_by=user)
            sql.save()
            my_message = {
                "status": "ok",
                "message": "successfuly uploaded "
            }
            mymessage_error = {
                "status": "no",
                "message": "something went wrong, try again"
            }

            return render(request, 'blogpost.html', context=my_message)

        else:
            mymessage_error = {
                "user_blank": "yes"
            }

            return render(request, 'blogpost.html', context=mymessage_error)



def blog_details(request, blog_id):
    my_blog_details = BlogPost.objects.filter(id=blog_id)
    makedictionary = {
        "single_data": my_blog_details
    }
    return render(request, "blogpostshow.html", context=makedictionary)


def image(request):
    if request.method == "GET":
        return render(request, 'image.html')

@csrf_exempt
def ajax_request(request):
    if request.method == "GET":
        return render(request, 'ajax_page.html')

    if request.method == "POST":
        # json_data = json.loads(request.body)
        #         # print(json_data["name"])
        #         # print(json_data["email"])

        name = request.POST['name']
        email = request.POST['email']
        print(name)
        print(email)

        sql = MyAjaxTest(name=name, email=email)
        sql.save()

        return JsonResponse({"success":"data received",})

