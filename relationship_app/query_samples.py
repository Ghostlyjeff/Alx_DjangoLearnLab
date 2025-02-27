import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    return []

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return [book.title for book in library.books.all()]
    return []

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library and hasattr(library, 'librarian'):
        return library.librarian.name
    return None

# Sample Usage
if __name__ == "__main__":
    print("Books by Author:", books_by_author("J.K. Rowling"))
    print("Books in Library:", books_in_library("Central Library"))
    print("Librarian for Library:", librarian_for_library("Central Library"))
