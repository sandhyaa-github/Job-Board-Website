from django.db import models

from user.models import UserProfile, EmployerProfile
from django.utils.text import slugify


STATUS_TYPES = [
    ('applied', 'Applied' ),
    ('viewed_by_recruiter','Viewed_by_recruiter'),
    ('shortlisted', 'Shortlisted'),
    ('not shortlisted','Not shortlisted'),
    ('awaiting for response', 'Awaiting for response'),
    ('selected','Selected'),
    ('not selected', 'Not selected')
]
# Create your models here.
class JobCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class JobListing(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name="posted_by")
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='job_category')
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(JobListing, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    applicant = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='applicant_profile')
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='jobs')
    resume = models.FileField(upload_to='job_applications/')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_TYPES, max_length=100)

    def __str__(self):
        return f"{self.applicant.user.username} - {self.job_listing.title}"