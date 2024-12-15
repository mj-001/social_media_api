"""
URL configuration for api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from api import views 

# Set up the router for the BookViewSet (use BookViewSet instead of BookList)
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book-list')  # Register BookViewSet


urlpatterns = [
    path('', views.home, name='home'),  # No leading slash here
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Assuming you have an 'api' app
    path('books/', views.BookList.as_view(), name='book-list'),  # Optional: Keep for specific list view
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
