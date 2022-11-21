from django.db import models

# Create your models here.
class Blog(models.Model):
    update_type = models.CharField(max_length = 200, help_text="Like a title")
    update_day = models.CharField(max_length = 200)
    blog_post = models.CharField(max_length = 100000)