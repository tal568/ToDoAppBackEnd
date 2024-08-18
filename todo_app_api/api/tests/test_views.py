from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import Group, Permissions, Task


class GroupTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create_user(username="test", password="test")
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

        group = Group.objects.create(name="test group", description="test description")
        Permissions.objects.create(user=user, level="owner", group=group)
        Task.objects.create(
            title="test task", description="test description", stage="todo", group=group
        )

    def test_get_groups(self):
        group = Group.objects.first()
        response = self.client.get(reverse("groups"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], group.name)

    def test_get_group(self):
        group = Group.objects.first()
        response = self.client.get(reverse("group", kwargs={"id": group.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], group.name)

    def test_get_non_existing_group(self):
        response = self.client.get(reverse("group", kwargs={"id": 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_group(self):
        group = Group.objects.first()
        response = self.client.delete(reverse("group", kwargs={"id": group.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Group.objects.count(), 0)

    def test_get_tasks(self):
        task = Task.objects.first()
        response = self.client.get(reverse("tasks", kwargs={"id": task.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], task.title)

    def test_create_task(self):
        group = Group.objects.first()
        data = {
            "title": "new task",
            "description": "new description",
            "stage": "todo",
            "group": group.id,
        }
        response = self.client.post(reverse("tasks"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_task(self):
        task = Task.objects.first()
        response = self.client.delete(reverse("tasks", kwargs={"id": task.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_get_permissions(self):
        permission = Permissions.objects.first()
        response = self.client.get(reverse("permissions", kwargs={"id": permission.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.first(), permission.user)

    def test_create_permission(self):
        user = User.objects.create_user(username="test2", password="test2")
        group = Group.objects.first()
        data = {"user": user.id, "level": "read", "group": group.id}
        response = self.client.post(reverse("permissions"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_jwt(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer")
        response = self.client.get(reverse("groups"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def doCleanups(self) -> None:
        return super().doCleanups()
