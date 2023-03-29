from django.urls import path
from todo_app import views

# from .views import home, TaskList, TaskDetail

urlpatterns = [
    path(
        "", 
        views.ItemListView.as_view(), 
        name="index"),
    path(
        "item/<int:pk>/",
        views.ItemDetailView.as_view(),
        name="item"),

    path(
        "item/<int:pk>/edit/",
        views.ItemUpdate.as_view(),
        name="item-update",
    ),

    # CRUD patterns for ToDoItems
    path(
        "item/add/",
        views.ItemCreate.as_view(),
        name="item-add",
    ),
    
]