# the urls of the api with django

from django.urls import path

from . import views

urlpatterns = [
    path('groups', views.groups, name="groups"),
    path('group/<int:id>', views.group, name="group"),
    path('task/<int:id>', views.tasks, name="tasks"),
    path('permission/<int:id>', views.permissions, name="permissions"),
   ]

