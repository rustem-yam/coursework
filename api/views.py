from rest_framework import status, generics, viewsets
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from rest_framework.decorators import action
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.conf import settings
from .serializers import (
    CreatePostSerializer,
    PostSerializer,
    CommentSerializer,
    CreateCommentSerializer,
)
from datetime import date
from .models import Post, Comment, Like

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


class PostsCreateView(LoginRequiredMixin, APIView):
    serializer_class = CreatePostSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if not (serializer.is_valid()):
            return Response(
                {"Bad Request": "Invalid data... %s" % serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        text = serializer.data.get("text")
        user = request.user
        creation_date = date.today()

        post = Post(text=text, user=user, creation_date=creation_date)

        post.save()
        return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)


# class PostsDeleteView(LoginRequiredMixin, APIView):
#     def delete(self, request, post_pk, format=None):
#         try:
#             post = Post.objects.get(pk=post_pk)
#         except Post.DoesNotExist:
#             return Response(
#                 {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
#             )

#         if post.user != request.user:
#             return Response(
#                 {"Error": "You do not have permission to delete this post"},
#                 status=status.HTTP_403_FORBIDDEN,
#             )

#         post.delete()
#         return Response(
#             {"Success": "Post deleted successfully"},
#             status=status.HTTP_204_NO_CONTENT,
#         )


# class PostsListView(APIView):
#     serializer_class = PostSerializer

#     def get(self, request, format=None):
#         limit = request.query_params.get("limit") or 10
#         page = request.query_params.get("page") or 1

#         posts = Post.objects.all().order_by("id")

#         paginator = Paginator(posts, limit)

#         try:
#             posts_page = paginator.page(page)
#         except Exception as e:
#             return Response(
#                 {"Bad Request": "Invalid page number"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         serializer = self.serializer_class(posts_page, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class PostsRetrieveView(APIView):
    serializer_class = PostSerializer

    def get(self, request, post_pk, format=None):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(
                {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostsViewSet(viewsets.ViewSet):
    serializer_class = PostSerializer

    @action(methods=["GET"], detail=False)
    def get_all(self, request):
        queryset = Post.objects.all().order_by("id")
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @action(methods=["POST"], detail=True)
    def delete(self, request, post_pk=None):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(
                {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if post.user != request.user:
            return Response(
                {"Error": "You do not have permission to delete this post"},
                status=status.HTTP_403_FORBIDDEN,
            )

        post.delete()
        return Response(
            {"Success": "Post deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class CommentsListsPostView(APIView):
    serializer_class = CommentSerializer

    def get(self, request, post_pk, format=None):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(
                {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        limit = request.query_params.get("limit") or 10
        page = request.query_params.get("page") or 1

        comments = Comment.objects.filter(post=post_pk).order_by("id")

        paginator = Paginator(comments, limit)
        try:
            comments_page = paginator.page(page)
        except Exception as e:
            return Response(
                {"Bad Request": "Invalid page number"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(comments_page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentsRetrieveView(APIView):
    serializer_class = CommentSerializer

    def get(self, request, post_pk, comment_pk, format=None):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(
                {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            comment = Comment.objects.get(post=post, pk=comment_pk)
        except Comment.DoesNotExist:
            return Response(
                {"Not Found": "Comment not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentsCreateView(LoginRequiredMixin, APIView):
    serializer_class = CreateCommentSerializer

    def post(self, request, post_pk, format=None):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(
                {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(data=request.data)
        if not (serializer.is_valid()):
            return Response(
                {"Bad Request": "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST
            )

        text = serializer.data.get("text")
        user = request.user
        creation_date = date.today()

        comment = Comment(text=text, user=user, creation_date=creation_date, post=post)
        comment.save()
        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)


class CommentsDeleteView(LoginRequiredMixin, APIView):
    def delete(self, request, post_pk, comment_pk, format=None):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(
                {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            comment = Comment.objects.get(post=post_pk, pk=comment_pk)
        except Comment.DoesNotExist:
            return Response(
                {"Not Found": "Comment not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if comment.user != request.user:
            return Response(
                {"Error": "You do not have permission to delete this comment"},
                status=status.HTTP_403_FORBIDDEN,
            )

        comment.delete()
        return Response(
            {"Success": "Comment deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class LikesPostView(APIView):
    def get(self, request, post_pk, format=None):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(
                {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )
        likes = Like.objects.filter(post=post)

        return Response(likes.count(), status=status.HTTP_200_OK)

    def post(self, request, post_pk, format=None):
        if not request.user.is_authenticated:
            login_url = reverse(settings.LOGIN_URL)
            return redirect(login_url)

        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(
                {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        user = request.user
        date_added = date.today()

        try:
            like = Like.objects.get(post=post, user=user)
            return Response(
                {"Error": "Like is already added"}, status=status.HTTP_400_BAD_REQUEST
            )
        except Like.DoesNotExist:
            pass

        like = Like(post=post, user=user, date_added=date_added)
        like.save()
        return Response(str(like), status=status.HTTP_201_CREATED)

    def delete(self, request, post_pk, format=None):
        if not request.user.is_authenticated:
            login_url = reverse(settings.LOGIN_URL)
            return redirect(login_url)

        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response(
                {"Not Found": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            like = Like.objects.get(post=post, user=request.user)
        except Like.DoesNotExist:
            return Response(
                {"Not Found": "Like not found"}, status=status.HTTP_404_NOT_FOUND
            )

        like.delete()
        return Response({"Success": "Like deleted"}, status=status.HTTP_204_NO_CONTENT)
