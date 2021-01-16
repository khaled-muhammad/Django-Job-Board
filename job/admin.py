from django.contrib import admin

# Register your models here.
from .models import job, job_category

admin.site.register(job)
admin.site.register(job_category)