# Create your views here.
from django.shortcuts import get_object_or_404
from django.test import TestCase
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Group, Task, Permissions
from .serializers import GroupSerializer, TaskSerializer, Permissionserializer


@api_view(['GET','POST'])
def groups(request):

    if request.method=='GET':
        groups=Group.objects.all()
        serializer=GroupSerializer(groups, many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
@api_view(['GET','PUT','DELETE'])
def group(request, id):
    if request.method=='GET':
        group=get_object_or_404(Group, id=id)
        serializer=GroupSerializer(group)
        return Response(serializer.data)
   
    if request.method=='DELETE':
        group=get_object_or_404(Group, id=id)
        group.delete()
        return Response(status=204)
    if request.method=='PUT':
        group=get_object_or_404(Group, id=id)
        serializer=GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tasks(request, id):
    if request.method == 'GET':
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    if request.method == 'DELETE':
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response(status=204)

    if request.method == 'PUT':
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def permissions(request, id):
    if request.method == 'GET':
        permission = get_object_or_404(Permissions, id=id)
        serializer = Permissionserializer(permission)
        return Response(serializer.data)

    if request.method == 'DELETE':
        permission = get_object_or_404(Permissions, id=id)
        permission.delete()
        return Response(status=204)

    if request.method == 'PUT':
        permission = get_object_or_404(Permissions, id=id)
        serializer = Permissionserializer(permission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'POST':
        serializer = Permissionserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
