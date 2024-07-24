# the urls of the api with django

from django.urls import path
from . import views

urlpatterns = [
    path('groups', views.groups, name="groups"),
    path('group/<int:id>', views.groups_id, name="groups_id"),
   ]

