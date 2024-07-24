# the urls of the api with django

from django.urls import path
from . import views

urlpatterns = [
    path('groups', views.Groups, name="groups"),
   ]

