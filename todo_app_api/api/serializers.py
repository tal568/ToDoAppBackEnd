# serializers.py

from rest_framework import serializers

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
    tasks = TaskSerializer(many=True, read_only=True)
    permisons = PermisonSerializer(many=True)

    class Meta:
        model = Group
        fields = ["id", "name", "description", "tasks", "permisons"]
    def create(self, validated_data):
        permisons_data = validated_data.pop('permisons', [])
        
        group = Group.objects.create(**validated_data)
        for permison_data in permisons_data:
            Permison.objects.create(group=group, **permison_data)

        
        return group

