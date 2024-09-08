from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.socialaccount.models import SocialApp
from django.shortcuts import redirect
from django.urls import reverse

from .serializers import UserSerializer



class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Redirect to Google OAuth after user signs up
            if SocialApp.objects.filter(provider='google').exists():
                return redirect(reverse('socialaccount_login', kwargs={'provider': 'google'}))
            return Response({
                'message': 'User created successfully',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)