from django.test import TestCase

from django.test import TestCase
from .models import Group, Task, Permissions

class TodoAppAPITestCase(TestCase):
    def setUp(self):
        # Create test data
        self.group = Group.objects.create(name='Test Group', description='Test description')
        self.task = Task.objects.create(title='Test Task', description='Test description', stage='In Progress', group=self.group)
        self.permission = Permissions.objects.create(user='testuser', level='readonly', group=self.group)

    def test_group_model(self):
        # Test the Group model
        self.assertEqual(self.group.name, 'Test Group')
        self.assertEqual(self.group.description, 'Test description')
        self.assertEqual(self.group.permissions.filter(user='testuser').values()[0]['user'], 'testuser')

    def test_task_model(self):
        # Test the Task model
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test description')
        self.assertEqual(self.task.stage, 'In Progress')
        self.assertEqual(self.task.group, self.group)

    def test_permission_model(self):
        # Test the Permissions model
        self.assertEqual(self.permission.user, 'testuser')
        self.assertEqual(self.permission.level, 'readonly')
        self.assertEqual(self.permission.group, self.group)

    def test_group_access_permission(self):
        # Test that a group can access its permissions
        permissions = self.group.permissions.all()
        self.assertEqual(permissions.count(), 1)
        self.assertEqual(permissions[0], self.permission)

    def test_permission_access_group(self):
        # Test that a permission can access its group
        group = self.permission.group
        self.assertEqual(group, self.group)

    def tearDown(self):
        # Clean up test data
        self.group.delete()
        self.task.delete()
        self.permission.delete()

