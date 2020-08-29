from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
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

def home(request):
    return render(request, 'admin_dash/index.html')