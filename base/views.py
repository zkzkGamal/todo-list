from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'Tasks'
    template_name = 'base/tasks.html'
    
class DetailList(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    
class CreateList(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class UpdateList(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class DeleteList(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'
