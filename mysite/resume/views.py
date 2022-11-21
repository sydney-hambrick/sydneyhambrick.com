from resume.models import Job
from django.views.generic import ListView

"""def index(request):
    job_name = Job.objects.all()
    context = {'job_name' : job_name}
    return render(request, 'index.html', context)"""

class index(ListView):
    model = Job
    context_object_name = "my_jobs"