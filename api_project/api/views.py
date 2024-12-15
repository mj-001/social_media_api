from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import generics.ListAPIView
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class BookList(ListAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")

