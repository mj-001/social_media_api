# relationship_app/views.py

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, UserProfile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test

# Function-based view for listing books
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(LoginRequiredMixin, DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Role-based views
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Permission-based views for book operations
@permission_required('relationship_app.can_add_book')
def add_book(request):
    # Add book logic here
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    # Edit book logic here
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    # Delete book logic here
    return render(request, 'relationship_app/delete_book.html')

# User Registration View
def UserCreationForm():
    form_class = UserCreationForm  # Use Django's built-in UserCreationForm
    template_name = 'relationship_app/register.html'  # Link to the register.html template
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
