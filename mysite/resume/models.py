from django.db import models
from datetime import date

class Job(models.Model):
    """Takes the name of a job"""
    job_name = models.CharField(max_length = 200, help_text="Enter name of job")
    business_name = models.CharField(max_length=200, help_text="Enter name of business")
    year_worked = models.CharField(max_length=200, help_text="Enter dates worked")
    job_description = models.CharField(max_length=1000, help_text="Enter job duties")

    class Meta:
        ordering = ["-year_worked"]
