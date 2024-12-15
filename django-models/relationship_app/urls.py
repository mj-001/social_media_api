from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Updated Login and Logout views with `template_name` specified in `urls.py`
    path('login/', views.UserLoginView.as_view(template_name='relationship_app/templates/login.html'), name='login'),
    path('logout/', views.UserLogoutView.as_view(template_name='relationship_app/templates/logout.html'), name='logout'),

    # Registration URL
    path('register/', views.register, name='register'),

    # Additional view URLs
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
