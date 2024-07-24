# Create your views here.
from django.test import TestCase
from .serializers import GroupSerializer, TaskSerializer, PermisonSerializer
from .models import Group, Task, Permison
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
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