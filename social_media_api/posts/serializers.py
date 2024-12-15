from  rest_framework import serializers
from .models import Post
from .models import Comment

class Postserializers(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')

    class Meta:
        model=Post
        fields=['id', 'author', 'title', 'content', 'created_at', 'updated_at']

class CommentSerializers(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')

    class Meta:
        model=Post
        fields=['id', 'author', 'title', 'content', 'created_at', 'updated_at']