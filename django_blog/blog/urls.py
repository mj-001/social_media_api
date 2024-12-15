from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CommentCreateView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', views.profile, name='profile'),
]


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),  # Updated URL pattern
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Post detail page
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),  # Create new comment
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_edit'),  # Edit comment
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),  # Delete comment
]

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.search, name='search'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
    #path('tag/<str:tag_name>/', views.tagged_posts, name='tagged_posts'),
]