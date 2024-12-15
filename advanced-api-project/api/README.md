## API Features: Filtering, Searching, and Ordering

### Endpoints
- `GET /api/books/`: Retrieve a list of books with advanced query capabilities.

### Query Parameters
1. **Filtering**:
   - Filter by publication year:
     ```
     /api/books/?publication_year=2023
     ```
   - Filter by author name:
     ```
     /api/books/?author__name=John%20Doe
     ```

2. **Searching**:
   - Search by title or author name:
     ```
     /api/books/?search=Django
     ```

3. **Ordering**:
   - Order by title (ascending):
     ```
     /api/books/?ordering=title
     ```
   - Order by publication year (descending):
     ```
     /api/books/?ordering=-publication_year
     ```

### Examples
- Get all books by "Jane Doe" published in 2023, ordered by title:


## Testing the API

Unit tests are implemented to ensure the correctness and reliability of the API.

### Running the Tests
Run the following command to execute the test suite:
```bash
python manage.py test api
