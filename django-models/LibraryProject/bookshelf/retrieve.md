# Retrieve and display all attributes of the book
retrieved_book = Book.objects.get(id=book.id)
# Expected output:
# <Book: 1984 by George Orwell (1949)>
