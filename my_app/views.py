from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Project, Task
from .forms import ProjectForm, TaskForm

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


def projects(request):
    if request.method == 'POST':
        forms = ProjectForm(request.POST or None)
        if forms.is_valid():
            forms.save()
            return redirect('home:home')
    else:
        forms = ProjectForm()
    return render(request, 'forms.html', {'forms': forms})


def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = TaskForm()
    return render(request, 'tarea.html', {'form': form})

def project_task(request, project_id):
    project = get_object_or_404(Project, name=project_id)
    task = Task.objects.filter(project=project)

    return render(request, 'project_task.html', {'project': project, 'tasks': task})

