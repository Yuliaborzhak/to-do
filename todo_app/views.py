# from django.shortcuts import render

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from .models import ToDoItem
from django.urls import reverse

# Create your views here.

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/index.html"

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
    #     return context

class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
    #     todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
    #     initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        # todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        # context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("index")

class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        # context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("index")    
