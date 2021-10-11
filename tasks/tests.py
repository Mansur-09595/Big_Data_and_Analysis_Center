from django.test import TestCase
from django.contrib.auth.models import User

from .models import Task
# Create your tests here.
class TaskTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        # Create a tasks
        test_task = Task.objects.create(
            author=testuser1, title='Task title', body='Task content...')
        test_task.save()

    def test_task_content(self):
        task = Task.objects.get(id=1)
        author = f'{task.author}'
        title = f'{task.title}'
        body = f'{task.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Task title')
        self.assertEqual(body, 'Task content...')