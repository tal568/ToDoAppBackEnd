# serializers.py

from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Group, Task, Permissions


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "stage"]


class Permissionserializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = ["id", "user", "level"]


class GroupSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    permissions = Permissionserializer(many=True, required=False)

    class Meta:
        model = Group
        fields = ["id", "name", "description", "tasks", "permissions"]

    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions',None)
        if permissions_data is None:
            raise ValidationError("permissions are required")
        group = Group.objects.create(**validated_data)
        for permission in permissions_data:
            Permissions.objects.create(group=group, **permission)
        return group
