from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import UserProfile, EmployerProfile

# Register your models here.
from django.contrib.auth.admin import UserAdmin

# class CustomUserAdmin(UserAdmin):
#     None
#     # Define custom admin options here

# admin.site.register(UserProfile, CustomUserAdmin)

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['user','bio','photo','dob']
#     search_fields = ['id','is_applicant','is_employer']
#     class Meta:
#         model = UserProfile
admin.site.register(UserProfile)


# class EmployerProfileAdmin(admin.ModelAdmin):
#     list_display = ['user','company_name','contact_email','phone_number', 'verified']
#     search_fields = ['id','is_applicant','is_employer', 'phone_number', 'verified']
#     class Meta:
#         model = EmployerProfile
admin.site.register(EmployerProfile)