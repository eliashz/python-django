from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    return HttpResponse("<h1>Holi, %s!</h1>" % username)

def about(request):
    return HttpResponse("About!")

