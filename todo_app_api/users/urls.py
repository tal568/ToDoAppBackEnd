

from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegistrationView

urlpatterns = [

path("accounts/", include("allauth.urls")),
    path("accounts/", include("allauth.socialaccount.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/",UserRegistrationView.as_view(),name="user_register")
    ]