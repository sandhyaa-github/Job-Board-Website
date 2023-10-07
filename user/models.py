from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from job_board import settings

class UserProfileManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, **extra_fields)

class UserProfile(AbstractUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_profile")
    bio = models.TextField(blank=True)
    current_address = models.CharField(max_length=120, blank=True)
    dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True)
    is_applicant = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    # REQUIRED_FIELDS = ['email']

    # objects = UserProfileManager()

    def __str__(self):
        return self.username


class EmployerProfile(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="employer_profile")
    company_name = models.CharField(max_length=200)
    company_description = models.TextField(blank=True)
    website = models.URLField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
