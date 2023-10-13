from rest_framework import generics
from .serializers import UserDetailSerializer, UserRegistrationSerializer
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