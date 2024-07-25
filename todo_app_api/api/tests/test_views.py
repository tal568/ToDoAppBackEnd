from django.test import TestCase,Client
from django.urls import reverse
from ..utils.create_group import create_group_with_permissions
from ..models import Group, Task, Permissions
from ..serializers import GroupSerializer
class GroupTests(TestCase):
    def setUp(self):
        self.client=Client()
        self.group=create_group_with_permissions({'name':'test group', 'description':'test description', 'permissions':[{"ghj"}]})
        



    def test_get_groups(self):
        response=self.client.get(reverse('groups'))
        self.assertEqual(response.status_code, 200)
       
