from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import GroupsView, GroupView, TasksView, PermissionsView


class TestUrl(SimpleTestCase):
    def test_url_groups_resolve(self):
        url = reverse("groups")
        self.assertEqual(resolve(url).func.view_class, GroupsView)

    def test_url_group_resolve(self):
        url = reverse("group", kwargs={"id": 1})
        self.assertEqual(resolve(url).func.view_class, GroupView)

    def test_url_permissions_resolve(self):
        url = reverse("permissions", kwargs={"id": 1})
        self.assertEqual(resolve(url).func.view_class, PermissionsView)

    def test_url_tasks_resolve(self):
        url = reverse("tasks", kwargs={"id": 1})
        self.assertEqual(resolve(url).func.view_class, TasksView)
