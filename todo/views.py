from django.shortcuts import render 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Todo
from django.urls import reverse_lazy


class TodoList(ListView):
    template_name = 'todo/list.html'
    model = Todo
    context_object_name = "tasks"

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"

class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")

class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")
