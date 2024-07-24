
from django.forms import ValidationError
from django.db.models import Model
from ..models import Group, Permissions
def create_group_with_permissions(validated_data:dict[str,Model])->Group:
        permissions_data = validated_data.pop('permissions')
        group = Group.objects.create(**validated_data)
        for permission in permissions_data:
            Permissions.objects.create(group=group, **permission)
        return group