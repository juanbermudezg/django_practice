from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
# Create your views here.
def index(request):
    title = "Django course!"
    return render(request, 'index.html', {
        'title':title
    })
def hello(request, username):
    print(type(username))
    return HttpResponse("<h1>Hello %s!<h1>"%username)
def about(request):
    username = 'juanb'
    return render(request, 'about.html',{
        'username':username
    })
def projects(request):
    projects=list(Project.objects.values())
    return render(request, 'projects.html',{
        'projects':projects
    })
def tasks(request):
    #task=get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks':tasks
    })