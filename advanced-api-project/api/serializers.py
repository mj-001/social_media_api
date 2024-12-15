from rest_framework import serializers
from .models import Author, Book
import datetime

# The BookSerializer serializes all fields of the Book model and includes validation for publication_year.
# The AuthorSerializer serializes the Author model and dynamically nests the serialized representation
# of related books using the BookSerializer.


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model, including validation for publication_year.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure the publication year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model, including nested serialization of books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
