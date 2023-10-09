# user/serializers.py

from rest_framework import serializers
from .models import UserProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'is_applicant', 'is_employer')

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_applicant=validated_data.get('is_applicant', False),
            is_employer=validated_data.get('is_employer', False),
        )
        return user
