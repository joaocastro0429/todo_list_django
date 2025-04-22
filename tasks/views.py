from django.shortcuts import render, redirect
from .models import Tasks

def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'index.html', {'tasks': tasks})  # <- Corrigido aqui

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Tasks.objects.create(title=title)
    return redirect('index')

def complete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('index')
