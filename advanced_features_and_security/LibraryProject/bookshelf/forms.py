from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=True)

class ExampleForm(forms.Form):
    """
    A simple example form for demonstration purposes.
    """
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    email = forms.EmailField(required=True, label="Your Email")
    message = forms.CharField(
        widget=forms.Textarea,
        max_length=500,
        required=True,
        label="Your Message"
    )

