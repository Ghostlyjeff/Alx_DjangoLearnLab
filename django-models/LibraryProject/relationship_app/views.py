from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  #  Ensure Library is imported

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  #  Fetch all books from the database
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Uses the Library model
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
 from .models import Library