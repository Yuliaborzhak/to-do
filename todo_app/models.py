from django.utils import timezone

from django.db import models
from django.urls import reverse

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

def mark_as_completed(request, pk):
    subtask = SubTask.objects.get(pk=pk)
    if request.method == "POST":
        subtask.title = request.POST.get("title")
        if request.POST.get("completed") == 'on':
            subtask.completed = True
        else:
            subtask.completed = False
        subtask.save()
        return HttpResponseRedirect(f"/edit-task/{subtask.task.id}/")

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    completed = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse(
    #         "item", args=[str(self.id)]
    #     )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]