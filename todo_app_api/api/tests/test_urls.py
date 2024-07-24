from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .. import views

class TestUrl(SimpleTestCase):
    def test_url_resolve(self):
        url = reverse('groups')
        self.assertEqual(resolve(url).func, views.groups)
        
       


    def test_url_resolve(self):
        url = reverse('group',kwargs={'id':1})
        self.assertEqual(resolve(url).func, views.group)
    
    def test_url_resolve(self):
        url = reverse('tasks',kwargs={'id':1})
        self.assertEqual(resolve(url).func, views.tasks)

    def test_url_resolve(self):
        url = reverse('permissions',kwargs={'id':1})
        self.assertEqual(resolve(url).func, views.permissions)