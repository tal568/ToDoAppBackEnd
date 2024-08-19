from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [

    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("", views.home, name="home"),
 ]