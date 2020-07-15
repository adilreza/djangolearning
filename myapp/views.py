from django.shortcuts import render

# Create your views here.

def index_file(request):
    return render(request, 'index.html')