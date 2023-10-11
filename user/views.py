from rest_framework import generics
from .serializers import UserDetailSerializer, UserRegistrationSerializer
from .models import Profile
# from .permissions import permissions


class UserRegistrationView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserDetailSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            self.serializer_class = UserRegistrationSerializer
        return super().get_serializer(*args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            self.serializer_class = UserRegistrationSerializer
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        super().get_queryset()
        queryset = Profile.objects.all()
        return queryset
