from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'admin_dash/index.html')
    
def user_login(request):
    if request.method == "GET":
        return render(request, 'admin_dash/login.html', {'success': True})
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            request.session['my_auth_user']=username
            return render(request, 'admin_dash/todo.html', {'success':True})
        else:
            return render(request, 'admin_dash/login.html', {'success': False})


def register(request):
    if request.method=="GET":
        return render(request, 'admin_dash/register.html')
    if request.method=="POST":
        if request.POST['password'] != request.POST['password2']:
            return render(request, 'admin_dash/register.html', {'not_match': True})
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        username = request.POST['username']
        usr = User.objects.create_user(username=username, email=email, password=password)
        usr.first_name = name
        usr.save()

        return JsonResponse({"message":"Successfully create a new user"})
