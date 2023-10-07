# user/urls.py

from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    # Add other authentication-related endpoints if needed
]
