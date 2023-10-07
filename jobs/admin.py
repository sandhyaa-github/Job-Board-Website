from django.contrib import admin

from jobs.models import JobCategory, JobListing, JobApplication

# Register your models here.

class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name']
    class Meta:
        model = JobCategory
admin.site.register(JobCategory)


class JobListingAdmin(admin.ModelAdmin):
    list_display = ['title','comapany_name', 'category', 'posted_by', 'created_at', 'location']
    search_fields = ['location', 'title', 'company_name', 'posted_by']
    class Meta:
        model = JobListing
admin.site.register(JobListing)


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant','job_listing', 'applied_at']
    search_fields = ['applicant','job_listing', 'applied_at']
    class Meta:
        model = JobApplication
admin.site.register(JobApplication)