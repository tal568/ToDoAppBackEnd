
from ..models import Group
from rest_framework.response import Response
from rest_framework import status
def check_permission_level(func):
      def wrapper(*args, **kwargs):
       print(kwargs)
       print(args)
       print(func.__name__)

       group=Group.objects.get(id=1)
       return func(*args, **kwargs)
       user_group_permission=group.permissions_set.filter(user="tal").first().level
      return wrapper