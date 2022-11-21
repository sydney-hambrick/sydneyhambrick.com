from django.urls import path
from resume.views import index

urlpatterns = [
    path('', index.as_view(), name='job_list.html')
]