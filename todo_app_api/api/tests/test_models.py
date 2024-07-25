from django.test import TestCase
from ..models import Group, Task, Permissions


class TestModels(TestCase):
    def setUp(self):
        self.group = Group(name='test group', description='test description')
        self.group.save()
        Permissions.objects.create(user='test', level='owner', group=self.group)
        Task.objects.create(title='test task', description='test description', stage='todo', group=self.group)

    def test_group(self):
        group = Group.objects.first()
        self.assertEqual(group.name, 'test group')
        self.assertEqual(group.description, 'test description')

    def test_task(self):
        task = Task.objects.first()
        self.assertEqual(task.title, 'test task')
        self.assertEqual(task.description, 'test description')
        self.assertEqual(task.stage, 'todo')
        self.assertEqual(task.group, self.group)

    def test_permissions(self):
        permission = Permissions.objects.first()
        self.assertEqual(permission.user, 'test')
        self.assertEqual(permission.level, 'owner')
        self.assertEqual(permission.group, self.group)