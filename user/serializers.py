# user/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class UserDetailSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'photo', 'dob',
                  'is_applicant', 'is_employer')


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')
