from homepage.models import Blog
from django.views.generic import ListView

class index(ListView):
    model = Blog
    context_object_name = "my_updates"

