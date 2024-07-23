# serializers.py

from rest_framework import serializers

from .models import Group, Task, Permison

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'stage', 'group']
    
class PermisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permison
        fields = ['id', 'user', 'level']
    
class GroupSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    permisons = PermisonSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'tasks', 'permisons']


