# Create your views here.
from django.test import TestCase
from .serializers import GroupSerializer, TaskSerializer, permissionserializer
from .models import Group, Task, Permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
   
@api_view(['GET','PUT','DELETE'])
def groups_id(request, id):
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
