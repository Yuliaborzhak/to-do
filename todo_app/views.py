# from django.shortcuts import render

from django.views.generic import ListView
from .models import ToDoItem

# Create your views here.

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/index.html"

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
    #     return context