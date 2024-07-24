# Create your views here.
from django.test import TestCase
from .serializers import GroupSerializer, TaskSerializer, permissionserializer
from .models import Group, Task, Permison
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

@api_view(['GET','POST','PUT'])
def Groups(request):

    if request.method=='GET':
        group=Group.objects.all()
        serializer=GroupSerializer(group, many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method=='PUT':
        group=get_object_or_404(Group, id=request.data.get('id'))
        serializer=GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)