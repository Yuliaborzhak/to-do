from django.utils import timezone

from django.db import models
from django.urls import reverse

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

# class ToDoList(models.Model):
#     title = models.CharField(max_length=100, unique=True)

#     def get_absolute_url(self):
#         return reverse("list", args=[self.id])

#     def __str__(self):
#         return self.title

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