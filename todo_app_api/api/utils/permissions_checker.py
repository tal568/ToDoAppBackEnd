
from todo_app_api.api.models import ActionType
from rest_framework import status
from rest_framework.response import Response
from todo_app_api.api.models import Group

def permissions_checker(action_type:ActionType,group_id,username):
    group_permissions=Group.objects.get(id=group_id).permissions
    user_permissions = group_permissions.filter(user=username)
    if(user_permissions>=action_type):
        return True
    raise Response(f"user has no permission to perform this action current permission is {user_permissions}",status.HTTP_403_FORBIDDEN)
    