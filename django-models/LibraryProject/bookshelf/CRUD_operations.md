# CRUD Operations Documentation

## Create
```python
from bookshelf.models import Book
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created book: {new_book}")

Created book: 1984

book = Book.objects.get(title="1984")
print(f"Title: {book.title}\nAuthor: {book.author}\nYear: {book.publication_year}")

Title: 1984
Author: George Orwell
Year: 1949

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")

Updated title: Nineteen Eighty-Four

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book exists after deletion?", Book.objects.filter(title="Nineteen Eighty-Four").exists())

Book exists after deletion? False