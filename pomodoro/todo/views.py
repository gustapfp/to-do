from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    task = Tasks.objects.all()
    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {
        'tasks': task,
        'form': form
    }
    return render(request, 'index.html', context)

def updateTasks(request, pk):
    task = Tasks.objects.get(id=pk)
    form = TasksForm(instance=task)

    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        'form': form
    }
    return render(request, 'update_tasks.html', context)

def deleteTasks(request, pk):
    item = Tasks.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect("/")

    context = {
        'item':item
    }
    return render(request, 'delete.html', context)