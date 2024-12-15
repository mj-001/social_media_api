from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Article
from .models import Book
from .forms import BookSearchForm
from .forms import ExampleForm

# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

@permission_required('bookshelf.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return redirect('article_list')
    return render(request, 'article_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('article_list')
    return render(request, 'article_form.html', {'article': article})

@permission_required('bookshelf.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

@permission_required('bookshelf.can_view_books', raise_exception=True)
def book_list(request):
    """
    Displays a list of books. Requires the user to have the 'can_view_books' permission.
    """
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def search_books(request):
    form = BookSearchForm(request.GET)
    books = []

    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)  # ORM handles SQL safely

    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})


def example_form_view(request):
    """
    Renders and processes the ExampleForm.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Add your logic here (e.g., save to database, send email)
            return render(request, 'bookshelf/form_success.html', {'name': name})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
