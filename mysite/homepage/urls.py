from django.urls import path
from homepage.views import index

urlpatterns = [
path('', index.as_view(), name="home")
]