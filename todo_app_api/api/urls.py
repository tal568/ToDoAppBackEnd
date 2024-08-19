# the urls of the api with django

from django.urls import path
from .views import GroupsView, GroupView, PermissionsView, TasksView

urlpatterns = [
    path("groups", GroupsView.as_view(), name="groups"),
    path("group/<int:id>", GroupView.as_view(), name="group"),
    path("group", GroupView.as_view(), name="group"),
    path("task/<int:id>", TasksView.as_view(), name="tasks"),
    path("task", TasksView.as_view(), name="tasks"),
    path("permissions/<int:id>", PermissionsView.as_view(), name="permissions"),
    path("permissions", PermissionsView.as_view(), name="permissions"),

]
