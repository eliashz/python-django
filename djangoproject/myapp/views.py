from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def hello(request, username):
    return HttpResponse("<h1>Holi, %s!</h1>" % username)

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def tasks(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasks.html')