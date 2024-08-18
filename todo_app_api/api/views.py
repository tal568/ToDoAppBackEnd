# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import ActionType, Group, Permissions, Task
from .serializers import GroupSerializer, PermissionSerializer, TaskSerializer
from .utils.permissions import require_permission


class GroupsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        groups = Group.objects.all().filter(permissions__user=request.user)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        require_permission(request.user, request.data["group"], ActionType.modify)
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class GroupView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        group = get_object_or_404(Group, id=id)
        require_permission(request.user, group.id, ActionType.read)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, id):
        group = get_object_or_404(Group, id=id)
        require_permission(request.user, group.id, ActionType.modify)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        group = get_object_or_404(Group, id=id)
        require_permission(request.user, group.id, ActionType.modify)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TasksView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        tasks = get_object_or_404(Task, id=id)
        require_permission(request.user, tasks.group.id, ActionType.read)
        serializer = TaskSerializer(tasks)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        require_permission(request.user, data["group"], ActionType.modify)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        task = get_object_or_404(Task, id=id)
        require_permission(request.user, task.group.id, ActionType.modify)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)
        require_permission(request.user, task.group.id, ActionType.modify)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PermissionsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        permissions = get_object_or_404(Permissions, id=id)
        require_permission(request.user, permissions.group.id, ActionType.read)
        serializer = PermissionSerializer(permissions)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data["user"] = str(request.user)
        action = ActionType.modify
        if data.get("level") == ActionType.owner:
            action = ActionType.owner
        require_permission(request.user, data["group"], action)
        serializer = PermissionSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        permission = get_object_or_404(Permissions, id=id)
        action = ActionType.modify
        if permission.level == ActionType.owner:
            action = ActionType.owner
        require_permission(request.user, permission.group.id, action)
        serializer = PermissionSerializer(permission, data=request.data)
        if serializer.is_valid():
            serializer.save(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        permission = get_object_or_404(Permissions, id=id)
        action = ActionType.modify
        if permission.level == ActionType.owner:
            action = ActionType.owner
        require_permission(request.user, permission.group.id, action)
        permission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
