from rest_framework import serializers
from .models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Post
        fields = (
            "id",
            "text",
            "user",
            "creation_date",
        )


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("text",)


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "user",
            "text",
            "creation_date",
        )


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("text",)
