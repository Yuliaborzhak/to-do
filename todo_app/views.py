# from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.shortcuts import render, redirect
from .models import ToDoItem
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def login_view(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        return HttpResponse("invalid credentials")
    
  return render(request, "registration/login.html", context)

def logout_view(request):
  logout(request)
  return redirect("index")


def mark_as_completed(request, pk):
    template_name = 'todo_app/completed.html'
    todo_Item = ToDoItem.objects.get(pk=pk)
    todo_Item.completed = True
    # todo_Item_update = ToDoItem.objects.filter(pk=pk).update(completed=True)
    # task.completed_ = timezone.now()
    todo_Item.save()
    return redirect('index')


# def mark_as_completed(request, pk):
#     todo_Item = ToDoItem.objects.get(pk=pk)
#     if request.method == "POST":
#         # todo_Item.title = request.POST.get("title")
#         if request.POST.get("completed") == 'on':
#             todo_Item.completed = True
#         else:
#             todo_Item.completed = False
#         todo_Item.save()
#         return HttpResponseRedirect("index")



class SignUp(CreateView):
   form_class = UserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'


class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/index.html"

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     return context

class ItemDetailView(DetailView):
    model = ToDoItem
    template_name = "todo_app/todoitem_detail.html"
    context_object_name = 'todo'

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     return context

    def get_reverse_url(self):
        return reverse(
            "item", args=[str(self.id)]
        )

class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "title",
        "description",
        "due_date",
        "completed",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
    #     todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
    #     initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self, **kwargs):
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
        "completed",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        # context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("index")    
        # return reverse("item", args=[self.object.todoitem_detail_id]) how to get the id of the detail page?
