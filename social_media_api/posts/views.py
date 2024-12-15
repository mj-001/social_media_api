from rest_framework import viewsets
from rest_framework import permissions
from .models import Post, Comment
from .serializers import Postserializers, CommentSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .models import Post, Like
from posts.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = Postserializers
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

def perform_create(self, serializer):
    from .models import Post  # Local import to avoid circular dependency
    serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        if not following_users.exists():
            return Response({"message": "You are not following anyone."}, status=200)

        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Fetch the post using get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        # Use get_or_create to ensure a like is created only if it doesn't already exist
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"error": "You already liked this post"}, status=HTTP_400_BAD_REQUEST)

        # Create a notification for the post's author
        notification = Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post,
            target_content_type=ContentType.objects.get_for_model(Post)
        )

        return Response({"message": "Post liked successfully"}, status=HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Fetch the post using get_object_or_404
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if the user has liked the post
        like = Like.objects.get_or_create(user=request.user, post=post)
        if not like:
            return Response({"error": "You have not liked this post"}, status=HTTP_400_BAD_REQUEST)

        # Remove the like
        like.delete()

        return Response({"message": "Post unliked successfully"}, status=HTTP_200_OK)