from rest_framework import serializers

from users.serializers import ProfileSerializer
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "profile", "post", "text")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")

class PostSerializer(serializers.ModelSerializer):
    # data 관리용 serializer
    profile = ProfileSerializer(read_only=True)
    # profile 내용을 갖고오기 위해 정의
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "profile", "title", "body", "image", "published_date", "likes", "comments")

class PostCreateSerializer(serializers.ModelSerializer):
    # 사용자 입력용 serializer
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")

