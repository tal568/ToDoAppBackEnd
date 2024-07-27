# serializers.py

from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Group, Permissions, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "stage", "group"]


class Permissionserializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions

        fields = ["id", "user", "level", "group"]


class GroupSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    permissions = Permissionserializer(many=True, required=False)

    class Meta:
        model = Group
        fields = ["id", "name", "description", "tasks", "permissions"]

    def create(self, validated_data)->Group:
        permissions_data = validated_data.pop("permissions", None)
        if permissions_data is None:
            raise ValidationError("permissions are required")
        group = Group.objects.create(**validated_data)
        for permission in permissions_data:
            Permissions.objects.create(group=group, **permission)
        return group
