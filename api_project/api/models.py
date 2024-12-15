from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  
    author = models.CharField(max_length=100)  
    published_date = models.DateField(null=True, blank=True)  
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)  
    pages = models.IntegerField(null=True, blank=True)  

    def __str__(self):
        return f"{self.title} by {self.author}"
