
from rest_framework.serializers import ModelSerializer  # Default serializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):  # Importing the default user serializer
    class Meta:
        model = User
        fields = ['id', 'username', 'email']