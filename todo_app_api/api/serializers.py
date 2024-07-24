# serializers.py

from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Group, Task, Permison

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id","title", "description", "stage"]
    
class PermisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permison
        fields = ["id", "user", "level"]
    
class GroupSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    permisons = PermisonSerializer(many=True,required=False)

    class Meta:
        model = Group
        fields = ["id", "name", "description", "tasks", "permisons"]
    def create(self, validated_data):

        permisons_data = validated_data.pop('permisons',None)
        if(permisons_data is None):
            raise ValidationError("permisons are required:user and level")
        
        group = Group.objects.create(**validated_data)
        permisons=Permison.objects.bulk_create([Permison(**data) for data in permisons_data])
        group.save()
        group.permisons.add(*permisons)

        
        return group
    def update(self,instance, validated_data):
        permisons_data = validated_data.pop('permisons',[])
        print(len(permisons_data))
        if(len(permisons_data)>0):
            instance.permisons.clear()
        task_data = validated_data.pop('tasks', [])
        if(len(task_data)>0):
            instance.tasks.clear()

        
        permisons=Permison.objects.bulk_create([Permison(**data) for data in permisons_data])
        tasks=Task.objects.bulk_create([Task(**data) for data in task_data])

        instance.permisons.add(*permisons)
        instance.tasks.add(*tasks)
        return super().update(instance, validated_data)

