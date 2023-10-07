# user/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer
from .models import UserProfile  # Import UserProfile model

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create a new user
        user = UserProfile.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
            is_applicant=serializer.validated_data.get('is_applicant', False),
            is_employer=serializer.validated_data.get('is_employer', False),
        )

        # Set the 'user' field of UserProfile to the user instance
        serializer.instance.user = user

        # Create a token for the user
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
