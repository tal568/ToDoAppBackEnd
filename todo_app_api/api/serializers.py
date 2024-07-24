# serializers.py

from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Group, Task, Permison

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id","title", "description", "stage"]
    
class permissionserializer(serializers.ModelSerializer):
    class Meta:
        model = Permison
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
        permissions=Permison.objects.bulk_create([Permison(**data) for data in permissions_data])
        group.save()
        group.permissions.add(*permissions)

        
        return group
    def update(self,instance, validated_data):
        permissions_data = validated_data.pop('permissions',[])
        print(len(permissions_data))
        if(len(permissions_data)>0):
            instance.permissions.clear()
        task_data = validated_data.pop('tasks', [])
        if(len(task_data)>0):
            instance.tasks.clear()

        
        permissions=Permison.objects.bulk_create([Permison(**data) for data in permissions_data])
        tasks=Task.objects.bulk_create([Task(**data) for data in task_data])

        instance.permissions.add(*permissions)
        instance.tasks.add(*tasks)
        return super().update(instance, validated_data)

