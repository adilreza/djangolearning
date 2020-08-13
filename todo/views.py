from django.shortcuts import render
from .models import todo_list
from django.views.decorators.csrf import csrf_exempt


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
        return render(request, 'todo.html')

def delete_task(request, id):
    if request.method == "GET":
        todo_list.objects.filter(id=id).delete()
        mydata = todo_list.objects.all()
        make_dictionary = {
            "all_data": mydata
        }
        return render(request,'todo.html',context=make_dictionary)