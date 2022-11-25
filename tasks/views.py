from django.shortcuts import render, redirect
from .models import *  #! this will access all the models
from .forms import *
import datetime
from django.db.models.functions import ExtractDay
from django.db.models import Count

import plotly.express as px
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

def searchTask(request):
    form = TaskForm()
    if request.method == 'POST':
        search = request.POST['search']
        tasks = Task.objects.filter(title__contains=search)
        context = {
            "tasks":tasks,
			"back":"back",
            "form":form
		}
        return render(request, 'main/index.html', context)
    else:
        return render(request, 'main/index.html', {})

def chartTask(request):
    template = 'main/chart.html'
    result = Task.objects.filter(created__year = '2022', created__month = '11').\
			annotate(day=ExtractDay('created'),\
				).values('day')\
					.annotate(TaskSum=Count('pk'))\
						.order_by('day')
    #! line chart
    fig = px.line(
        x=[str(i['day']) for i in result ],        #! [ 21,22,23,24,25]
        y=[i['TaskSum'] for i in result],          #! [0,0,0,7,0]
        title="Monthly Chart of To Do List",
        labels={ 'x': 'Day in a month', 'y': 'Number of To Do items'},
    )
    fig.update_layout(title={
            'font_size':22,
            'xanchor':'center',
            'x':0.5
    })
    #! bar chart
    fig1 = px.bar(
        x=[str(i['day']) for i in result ],        #! [ 21,22,23,24,25]
        y=[i['TaskSum'] for i in result],          #! [0,0,0,7,0]
        title="Monthly Chart of To Do List",
        labels={ 'x': 'Day in a month', 'y': 'Number of To Do items'},
    )
    fig1.update_layout(title={
            'font_size':22,
            'xanchor':'center',
            'x':0.5
    })
    chart = fig.to_html()
    bar = fig1.to_html()
    context = {
        "chart":chart,
        "bar":bar
    }
    return render (request, template, context)
