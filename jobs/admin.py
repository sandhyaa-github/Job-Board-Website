from django.contrib import admin

from jobs.models import JobCategory, JobListing, JobApplication


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

    class Meta:
        model = JobCategory


@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_name', 'category',
                    'posted_by', 'created_at', 'location']
    search_fields = ['location', 'title', 'company_name', 'posted_by']
    list_filter = ['location', 'title', 'company_name', 'posted_by']

    class Meta:
        model = JobListing


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job_listing', 'applied_at']
    search_fields = ['applicant', 'job_listing', 'applied_at']
    list_filter = ['applicant', 'job_listing', 'applied_at']

    class Meta:
        model = JobApplication
