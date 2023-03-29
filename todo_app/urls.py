from django.urls import path
from todo_app import views

urlpatterns = [
    path("", views.ItemListView.as_view(), name="index"),
    # CRUD patterns for ToDoItems
    path(
        "item/add/",
        views.ItemCreate.as_view(),
        name="item-add",
    ),
    path(
        "item/<int:pk>/",
        views.ItemUpdate.as_view(),
        name="item-update",
    ),
]