from django.test import TestCase

# Create your tests here.
# from django.test import TestCase
# from django.contrib.auth.models import User
from ..models import TaskList,UserModelBlog


class TaskListModelTest(TestCase):
    def setUp(self):

        self.user1 = UserModelBlog.objects.create(username='user1',password='123456')
        self.user2 = UserModelBlog.objects.create(username='user2', password='1234567')

        self.task = TaskList.objects.create(comment='This is a test task')
        self.task.who.set([self.user1, self.user2])

    def test_tasklist_creation(self):
        """Test if a TaskList instance is created properly."""
        self.assertEqual(self.task.comment, 'This is a test task')
        self.assertEqual(self.task.who.count(), 2)
        self.assertIn(self.user1, self.task.who.all())
        self.assertIn(self.user2, self.task.who.all())

    def test_tasklist_auto_now_add(self):
        """Test if the date field is automatically set on creation."""
        self.assertIsNotNone(self.task.date)

    def test_tasklist_str_method(self):
        """Test the __str__ method of the TaskList model."""
        self.assertEqual(str(self.task), 'This is a test task')
