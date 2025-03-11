import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from tasks.models import Task, Status


# Create your views here.

#home(request)
def home(request):
    return render(request, 'home.html')

#create_task(request)
def create_task(request):
    return render(request, 'tasks/create.html')

#list_tasks(request)
def list_tasks(request):
    return render(request, 'tasks/list.html')

#edit_task(request, task_id)
def edit_task(request, task_id):
    return render(request, 'tasks/edit.html')

#delete_task(request, task_id)
def delete_task(request, task_id):
    return render(request, 'tasks/delete.html')