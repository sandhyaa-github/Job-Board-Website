from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import Profile, EmployerProfile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'photo', 'active',
                    'dob', 'is_applicant', 'is_employer']
    search_fields = ['id', 'user', 'is_applicant', 'is_employer']
    list_filter = ['user', 'is_applicant', 'is_employer', 'active']

    class Meta:
        model = Profile


@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name',
                    'contact_email', 'phone_number', 'verified']
    search_fields = ['id', 'phone_number', 'verified']
    list_filter = ['company_name', 'contact_email', 'phone_number', 'verified']

    class Meta:
        model = EmployerProfile
