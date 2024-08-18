from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from ..models import ActionType, Group, Permissions


def user_has_permission(user, group, action_type):
    try:
        permission = Permissions.objects.get(user=user, group=group)
    except Permissions.DoesNotExist:
        return False

    return ActionType[permission.level] >= action_type


def require_permission(user, group_id, action_type):
    group = get_object_or_404(Group, id=group_id)
    if not user_has_permission(user, group, action_type):
        raise PermissionDenied("You do not have the required permission.")
