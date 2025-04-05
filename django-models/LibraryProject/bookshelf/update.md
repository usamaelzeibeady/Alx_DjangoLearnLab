
# Update Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(pk=book.id)
print(f"Updated title: {updated_book.title}")

Updated title: Nineteen Eighty-Four