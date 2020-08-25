from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from todo.models import TodoList
# Create your views here.

@csrf_exempt
def todo(request):
    if request.method == "GET":
        tasks = TodoList.objects.all()
        make_dictinary = {
            "all_data": tasks
        }
        return render(request, 'todo/todo.html', context=make_dictinary)
    if request.method == "POST":
        if request.method == "POST":
            usr = request.session.get('my_auth_user')
        
            if usr:
                task = request.POST['task']
                user = User.objects.get(username=request.session['my_auth_user'])

                sql = TodoList(task=task, user=user)
                sql.save()
                return JsonResponse({"success":"ok done "})

def todo_get(request):
    if request.method == "GET":
        usr = request.session.get('my_auth_user')
        user_ino = User.objects.filter(username=usr)
        for u in user_ino:
            user_id = u.id

        tasks = TodoList.objects.filter(user=user_id)
        html_var= ""
        for single_task in tasks:
            delete = "<a class='' href = '/deletetask/"+ str(single_task.id) +"' ><i class='fas fa-trash-alt'></i></a>"
            list_var = "<p class=''>"+ delete + "    " + single_task.task + "</p>"

            html_var=html_var + list_var + "<br/>"
        return HttpResponse(html_var)

def delete_task(request, id):
    if request.method == "GET":
        TodoList.objects.filter(id=id).delete()
        mydata = TodoList.objects.all()
        make_dictionary = {
            "all_data": mydata
        }
        return render(request,'todo/todo.html',context=make_dictionary)

def register(request):
    if request.method=="GET":
        return render(request, 'todo/register.html')
    if request.method=="POST":

        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        usr = User.objects.create_user(username=username, email=email, password=password)
        usr.save()
        return JsonResponse({"message":"Successfully create a new user"})


def todo_login(request):
    if request.method == "GET":
        return render(request, 'todo/login.html', {'success': True})
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            request.session['my_auth_user']=username
            return render(request, 'todo/todo.html', {'success':True})
        else:
            return render(request, 'todo/login.html', {'success': False})


def our_test(request):
    usr = request.session.get('my_auth_user')
    user_ino = User.objects.filter(username=usr)
    print(user_ino)
    return JsonResponse({"message":"Hello forom out test"})
