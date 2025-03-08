from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden

# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Views with access restrictions
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_dashboard.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_dashboard.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_dashboard.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm  # Ensure you have a form for adding/editing books

# View to add a book (only for users with "can_add_book" permission)
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after adding
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

# View to edit a book (only for users with "can_change_book" permission)
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

# View to delete a book (only for users with "can_delete_book" permission)
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})
