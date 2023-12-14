from django.urls import path
from .views import hello_django

urlpatterns = [
    path('hello/', hello_django, name='hello_django'),
]
