from rest_framework import serializers
from .models import Post


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
    id = serializers.IntegerField()

    class Meta:
        model = Post
        fields = (
            "id",
            "text",
        )
