from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

book_list_create_view = BookViewSet.as_view({'get': 'list', 'post': 'create'})


