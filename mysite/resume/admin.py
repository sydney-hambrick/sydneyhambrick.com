from django.contrib import admin
from resume.models import Job

class JobAdmin(admin.ModelAdmin):
    pass

admin.site.register(Job, JobAdmin)