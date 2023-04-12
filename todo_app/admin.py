from django.contrib import admin
from todo_app.models import ToDoItem
from django.contrib.auth.models import User
from operator import itemgetter
from django.db.models import Count

@admin.action(description='Assign unassigned tasks')
def assign_unassigned_tasks(self, request, queryset):
    unassigned_tasks = queryset.filter(user__isnull=True)
    users = User.objects.all().exclude(is_superuser=True)
    user_len_combined_list = []
    for user in users:
        tasks_count = user.tasks.all().count()
        user_len_list = {
        "name" : user.username,
        "tasks_num": tasks_count
        }
        user_len_combined_list.append(user_len_list)

    min_value = min(user_len_combined_list, key=itemgetter('tasks_num'))
    user_with_min_tasks = User.objects.get(username=min_value["name"])
    
    for task in unassigned_tasks:
        user_with_min_tasks.tasks.add(task)
   

class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    ordering = ['title']
    actions = [assign_unassigned_tasks]


# Register your models here.
admin.site.register(ToDoItem, ToDoItemAdmin)