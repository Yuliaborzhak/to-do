from django.test import TestCase

# Create your tests here.

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


    # def test_animals_can_speak(self):
    #     """Animals that can speak are correctly identified"""
    #     lion = Animal.objects.get(name="lion")
    #     cat = Animal.objects.get(name="cat")
    #     self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')