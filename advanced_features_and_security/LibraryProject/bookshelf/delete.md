# delete.md

```python
# Import the Book model
from bookshelf.models import Book

# Assuming the book to delete is already created, retrieve it first (for example by ID)
book = Book.objects.get(id=<book_id>)  # Replace <book_id> with the actual ID if known

# Delete the book instance
book.delete()

# Attempt to retrieve all books to confirm deletion
Book.objects.all()
# Expected output:
# <QuerySet []>
