from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.

def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    return HttpResponse("<h1>Holi, %s!</h1>" % username)

def about(request):
    return HttpResponse("About!")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = Task.objects.get(id=id)
    return HttpResponse('task:  %s'% task.title)