# Create your tests here.
import datetime
from django.utils import timezone
from django.test import TestCase
from django.core.exceptions import ValidationError
from todo_app.models import ToDoItem

class ToDoItemTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
            #Set up non-modified objects used by all test methods
            ToDoItem.objects.create(title='Learn Django in a week', description='Start with putting on your supercostume')

    def test_title_label(self):
            toDoItem=ToDoItem.objects.get(id=1)
            field_label = toDoItem._meta.get_field('title').verbose_name
            self.assertEquals(field_label,'title')

    def test_description_label(self):
            toDoItem=ToDoItem.objects.get(id=1)
            field_label = toDoItem._meta.get_field('description').verbose_name
            self.assertEquals(field_label,'description')

    def test_due_date_label(self):
            toDoItem=ToDoItem.objects.get(id=1)
            field_label = toDoItem._meta.get_field('due_date').verbose_name
            self.assertEquals(field_label,'due date')

    def test_title_max_length(self):
            toDoItem=ToDoItem.objects.get(id=1)
            max_length = toDoItem._meta.get_field('title').max_length
            self.assertEquals(max_length,100)

    def test_get_absolute_url(self):
            toDoItem=ToDoItem.objects.get(id=1)
            #This will also fail if the urlconf is not defined.
            self.assertEquals(toDoItem.get_absolute_url(),'todo_app/todoitem/1')
    
# Don't know how to  test if in clean()        
#     def test_clean_exception(self):
#         toDoItem = ToDoItem.objects.get(id=1)
#         # due_date = self.due_date.replace(tzinfo=utc)
#         # today_date = datetime.datetime.today().replace(tzinfo=utc)
#         with self.assertRaises(ValidationError) as exception_context:
#             toDoItem.clean()
#         self.assertEqual(
#             str(exception_context.exception),
#             "The date cannot be in the past!"
#         )    