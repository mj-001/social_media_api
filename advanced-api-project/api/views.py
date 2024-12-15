from django.shortcuts import render, filters
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

# Create your views here.

class BookListView(generics.ListAPIView):
    """
    Handles listing all Book instances with filtering, searching, and ordering capabilities.

    List all books with advanced query capabilities:
    - Filtering: Use query parameters to filter by title, author name, or publication year.
    - Searching: Search for books by title or author name.
    - Ordering: Sort results by title or publication year.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,  # For filtering
        filters.SearchFilter,  # For searching
        filters.OrderingFilter,  # For ordering
    ]

    # Define filtering fields
    filterset_fields = ['title', 'author__name', 'publication_year']  # Nested relationship for author

    # Define searchable fields
    search_fields = ['title', 'author__name']

    # Define ordering fields
    ordering_fields = ['title', 'publication_year']



class BookDetailView(generics.RetrieveAPIView):
    """
    Handles retrieving a single Book instance by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access for all


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Customize the creation of a book.
        """
        serializer.save()  # Add logic here if needed


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Customize the update of a book.
        """
        serializer.save()  # Add logic here if needed



class BookDeleteView(generics.DestroyAPIView):
    """
    Handles deleting a Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete
