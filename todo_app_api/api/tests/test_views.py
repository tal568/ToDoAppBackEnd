from django.test import TestCase
from django.urls import reverse
from ..models import Group, Task, Permissions
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class GroupTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create(username="test", password="test")
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        group = Group(name="test group", description="test description")
        group.save()
        Permissions.objects.create(user="test", level="owner", group=group)
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

    # todo test create group

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
        data = {"title": "new task", "description": "new description", "stage": "todo"}
        response = self.client.post(reverse("tasks", kwargs={"id": 1}), data)
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
        self.assertEqual(response.data["user"], permission.user)

    def test_create_permission(self):
        data = {"user": "new user", "level": "readonly"}
        response = self.client.post(reverse("permissions", kwargs={"id": 1}), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
