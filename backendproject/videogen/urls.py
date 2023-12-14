# videogen/urls.py

from django.urls import path
from .views import VideoGenerationView

urlpatterns = [
    path('generate-video/', VideoGenerationView.as_view(), name='generate-video'),
]
