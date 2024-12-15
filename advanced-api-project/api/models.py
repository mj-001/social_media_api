from django.db import models

# Create your models here.
# The Author model represents writers, with a one-to-many relationship to Book.
# Each Author can have multiple related Books.
# The Book model includes details about individual books, linking each to a specific Author.


class Author(models.Model):
    """
    Represents an author in the database.
    """
    name = models.CharField(max_length=100, help_text="Name of the author")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book associated with an author.
    """
    title = models.CharField(max_length=200, help_text="Title of the book")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', help_text="The author of the book")

    def __str__(self):
        return f"{self.title} by {self.author.name}"
