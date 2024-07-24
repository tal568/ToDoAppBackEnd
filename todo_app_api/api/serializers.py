# serializers.py

from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Group, Task, Permissions

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id","title", "description", "stage"]
    
class permissionserializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = ["id", "user", "level"]
    
class GroupSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    permissions = permissionserializer(many=True,required=False)

    class Meta:
        model = Group
        fields = ["id", "name", "description", "tasks", "permissions"]
    def create(self, validated_data):

        permissions_data = validated_data.pop('permissions',None)
        if(permissions_data is None):
            raise ValidationError("permissions are required:user and level")
        
        group = Group.objects.create(**validated_data)
        permissions=Permissions.objects.bulk_create([Permissions(**data) for data in permissions_data])
        group.save()
        group.permissions.add(*permissions)

        
        return group


