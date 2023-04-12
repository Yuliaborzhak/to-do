import datetime
import pytz
from django.core.exceptions import ValidationError

from django.utils import timezone

from django.db import models
from django.urls import reverse

from django import forms

from django.contrib.auth.models import User
from django.db.models import Avg

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

def clean_due_date(self):
    pass
        # date = self.cleaned_data["due_date"]
        # if date < datetime.date.today():
        #     raise forms.ValidationError({'bark_volume': ["The date cannot be in the past!",]})
        # return date

def get_superuser():
    su_user = User.objects.filter(is_superuser=True).first()
    if su_user:
        return su_user
    raise DoesNotExist('Please add Super User')  

# def completed_tasks(user):
#     return user.tasks.filter(completed=True).count()

# def unfinished_tasks(user):
#     return user.tasks.filter(completed=False).count()

# def after_due_tasks(user):
#     after_due_tasks = 0
#     for task in user.tasks:
#         if task.due_date < timezone.now() & task.completed == False:
#             after_due_tasks += 1
    
#     return after_due_tasks

# def avg_days_to_complete(user):
#     task.due_date - timezone.now()
#     Book.objects.aggregate(Avg('price'))

#     user.tasks.filter(completed=True).count()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # completed_tasks = models.IntegerField(default=completed_tasks(user))
    # unfinished_tasks = models.IntegerField(default=unfinished_tasks(user))
    # after_due_tasks = models.IntegerField(default=after_due_tasks(user))
    # avg_days_to_complete = 



class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    completed = models.BooleanField(default=False)
    completed_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET(get_superuser),
        related_name="tasks",
        null=True
        )

    # def get_absolute_url(self):
    #     return reverse(
    #         "item", args=[str(self.id)]
    #     )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    def clean(self):
        utc = pytz.UTC
        due_date = self.due_date.replace(tzinfo=utc)
        today_date = datetime.datetime.today().replace(tzinfo=utc)
        
        if due_date < today_date:
            raise ValidationError({'due_date': ["The date cannot be in the past!",]})
        
    class Meta:
        ordering = ["due_date"]