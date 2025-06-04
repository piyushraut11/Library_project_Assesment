from rest_framework import generics
from .models import Book, Author, Publisher
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherListCreateView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.select_related('publisher').prefetch_related('authors')
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related('publisher').prefetch_related('authors')
    serializer_class = BookSerializer