from django.shortcuts import render
from .models import todo_list
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.

@csrf_exempt
def todo(request):
    if request.method == "GET":
        tasks = todo_list.objects.all()
        make_dictinary = {
            "all_data": tasks
        }
        return render(request, 'todo.html', context=make_dictinary)
    if request.method == "POST":
        task = request.POST['task']
        sql = todo_list(task=task)
        sql.save()
        return JsonResponse({"success":"ok done "})

def todo_get(request):
    if request.method == "GET":
        tasks = todo_list.objects.all()
        html_var= ""
        for single_task in tasks:
            list_var = "<p class='btn btn-primary'>"+ single_task.task +"</p>"
            html_var=html_var+list_var+"<br/>"
        return HttpResponse(html_var)

def delete_task(request, id):
    if request.method == "GET":
        todo_list.objects.filter(id=id).delete()
        mydata = todo_list.objects.all()
        make_dictionary = {
            "all_data": mydata
        }
        return render(request,'todo.html',context=make_dictionary)

