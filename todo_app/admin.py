from django.contrib import admin
from todo_app.models import ToDoItem
from django.contrib.auth.models import User
from operator import itemgetter
from django.db.models import Count

@admin.action(description='Assign unassigned tasks')
def assign_unassigned_tasks(self, request, queryset):
    unassigned_tasks = queryset.filter(user__isnull=True).values()
    users = User.objects.all()
    user_len_combined_list = []
    for user in users:
        # there is a mistake in getting the number of user tasks + use queryset
        # q = User.objects.select_related('ToDoItem').annotate(num_toDoItem=Count('tasks'))
        user_len_list = {
        "name" : user.username,
        "task_len": user.num_toDoItem 
        }
        user_len_combined_list.append(user_len)
    min_value = min(user_len_combined_list, key=itemgetter('task_len'))
    user_with_min_tasks = min_value.name
    # unassigned_tasks.username = user_with_min_tasks - something like this
     
    print(users)
    print(user_len_combined_list)
    print(min_value)
    print(user_with_min_tasks)
 

class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    ordering = ['title']
    actions = [assign_unassigned_tasks]


# Register your models here.
admin.site.register(ToDoItem, ToDoItemAdmin)