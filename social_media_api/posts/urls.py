from django.urls import path 
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from .views import CommentViewSet
from .views import FeedView
from .views import LikePostView, UnlikePostView
from .views import NotificationView, MarkAsReadView

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
    path('notifications/', NotificationView.as_view(), name='notifications'),
    path('notifications/<int:pk>/read/', MarkAsReadView.as_view(), name='mark_as_read'),

]
