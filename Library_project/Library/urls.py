from django.urls import path
from .views import (
    AuthorListCreateView, AuthorDetailView,
    PublisherListCreateView, PublisherDetailView,
    BookListCreateView, BookDetailView
)

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('publishers/', PublisherListCreateView.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher-detail'),
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]