# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .utils.cheak_permission_level import check_permission_level
from .models import ActionType, Group, Permissions, Task
from .serializers import GroupSerializer, Permissionserializer, TaskSerializer


class GroupsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class GroupView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        group = get_object_or_404(Group, id=id)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, id):
        group = get_object_or_404(Group, id=id)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        group = get_object_or_404(Group, id=id)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TasksView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        tasks = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(tasks)
        return Response(serializer.data)

    def post(self, request, id):
        data = request.data.copy()
        data["group"] = id
        serializer = TaskSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PermissionsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        permissions = get_object_or_404(Permissions, id=id)
        serializer = Permissionserializer(permissions)
        return Response(serializer.data)

    def post(self, request, id):
        data = request.data.copy()
        print(request.user)

        data["user"] = str(request.user)
        data["group"] = id
        serializer = Permissionserializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        permission = get_object_or_404(Permissions, id=id)
        serializer = Permissionserializer(permission, data=request.data)
        if serializer.is_valid():
            serializer.save(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    @check_permission_level
    def delete(self, request, id):
        permission = get_object_or_404(Permissions, id=id)
        permission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
