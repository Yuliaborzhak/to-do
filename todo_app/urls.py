from django.urls import path
from todo_app import views

# from .views import home, TaskList, TaskDetail

urlpatterns = [
    path(
        "", 
        views.ItemListView.as_view(), 
        name="index"),
    path(
        "signup/", 
        views.SignUp.as_view(), 
        name="signup"),
    path(
        "login/", 
        views.login_view, 
        name="login"),
    path(
        "logout/", 
        views.logout_view, 
        name="logout"),      
    path(
        "item/<int:pk>/",
        views.ItemDetailView.as_view(),
        name="item"),

    path(
        "item/<int:pk>/edit/",
        views.ItemUpdate.as_view(),
        name="item-update",
    ),
    path(
        "item/<int:pk>/completed/",
        views.mark_as_completed,
        name="item-completed",
    ),

    # CRUD patterns for ToDoItems
    path(
        "item/add/",
        views.ItemCreate.as_view(),
        name="item-add",
    ),
    
]