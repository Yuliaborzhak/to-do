# from django.shortcuts import render

from django.views.generic import ListView
from .models import ToDoItem

# Create your views here.

class ListListView(ListView):
    model = ToDoItem
    template_name = "todo_app/index.html"