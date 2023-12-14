from django.urls import path
from task.views import index
from .views import BookListCreateView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('hello/',index, name = "index"),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
