from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserDetailSerializer, UserLoginSerializer, UserRegistrationSerializer
from .models import Profile

# from .permissions import permissions


class UserRegistrationView(generics.ListCreateAPIView):
    serializer_class = UserDetailSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            self.serializer_class = UserRegistrationSerializer
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        queryset = Profile.objects.all()
        return queryset


class LoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'username': user.username,
                    'user_id': user.id,
                })

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
