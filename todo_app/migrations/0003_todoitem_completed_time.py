# Generated by Django 3.2.9 on 2023-04-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todoitem_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='completed_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
