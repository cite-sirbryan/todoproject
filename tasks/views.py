from django.shortcuts import render, redirect
from .models import *  #! this will access all the models
from .forms import *
import datetime
# Create your views here.

def index(request):
    template = 'main/index.html'
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {
        "tasks": tasks,
        "form": form,
        "datenow": datetime.datetime.now(),
    }
    return render (request, template, context)

def updateTask(request, pk):
    template = 'main/update_task.html'
    
    tasks = Task.objects.get(id=pk)
    
    form = TaskForm(instance = tasks)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = tasks)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {
        "form": form
    }
    return render (request, template, context)

def deleteTask(request, pk):
    template = 'main/delete.html'
    tasks = Task.objects.get(id=pk)

    if request.method == 'POST':
        tasks.delete()
        return redirect('/')
    
    context = {
        "tasks": tasks
    }
    return render (request, template, context)
