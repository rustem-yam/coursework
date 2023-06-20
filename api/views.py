from rest_framework import status, generics
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import CreatePostSerializer, PostSerializer
from datetime import date
from .models import Post

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


class CreatePostView(LoginRequiredMixin, APIView):
    serializer_class = CreatePostSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if not (serializer.is_valid()):
            return Response(
                {"Bad Request": "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST
            )

        text = serializer.data.get("text")
        user = request.user
        creation_date = date.today()

        post = Post(text=text, user=user, creation_date=creation_date)

        post.save()
        return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)


class ListPostsView(APIView):
    serializer_class = PostSerializer

    def get(self, request, format=None):
        limit = request.query_params.get("limit") or 10
        page = request.query_params.get("page") or 1

        posts = Post.objects.all()

        paginator = Paginator(posts, limit)

        try:
            posts_page = paginator.page(page)
        except Exception as e:
            return Response(
                {"Bad Request": "Invalid page number"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(posts_page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrievePostView(APIView):
    serializer_class = PostSerializer

    def get(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(
                {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
