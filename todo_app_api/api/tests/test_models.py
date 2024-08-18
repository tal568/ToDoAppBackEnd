from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Group, Permissions, Task


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.group = Group.objects.create(
            name="test group", description="test description"
        )
        Permissions.objects.create(user=self.user, level="owner", group=self.group)
        Task.objects.create(
            title="test task",
            description="test description",
            stage="todo",
            group=self.group,
        )

    def test_group(self):
        group = Group.objects.first()
        self.assertEqual(group.name, "test group")
        self.assertEqual(group.description, "test description")

    def test_task(self):
        task = Task.objects.first()
        self.assertEqual(task.title, "test task")
        self.assertEqual(task.description, "test description")
        self.assertEqual(task.stage, "todo")
        self.assertEqual(task.group, self.group)

    def test_permissions(self):
        permission = Permissions.objects.first()
        self.assertEqual(permission.user, self.user)
        self.assertEqual(permission.level, "owner")
        self.assertEqual(permission.group, self.group)
