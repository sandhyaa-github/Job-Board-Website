from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import BaseUserManager

from job_board import settings


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', db_index=True)
    bio = models.TextField(blank=True, null=True)
    current_address = models.CharField(max_length=120, blank=True)
    mobile_no = models.BigIntegerField(null=False, blank=False, db_index=True)
    dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="profile_photos/", blank=True)
    is_applicant = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        pass

    def __str__(self):
        return self.user.username


class EmployerProfile(models.Model):
    user = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="employer_profile")
    company_name = models.CharField(max_length=200)
    company_description = models.TextField(blank=True)
    website = models.URLField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name
