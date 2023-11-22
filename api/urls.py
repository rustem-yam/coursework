from django.urls import path
from .views import (
    PostsCreateView,
    PostsListView,
    PostsRetrieveView,
    PostsDeleteView,
    CommentsListsPostView,
    CommentsRetrieveView,
    CommentsCreateView,
    CommentsDeleteView,
    LikesPostView,
)

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Posts
    path("posts/create/", PostsCreateView.as_view(), name="create-post"),
    path("posts/", PostsListView.as_view(), name="list-posts"),
    path("posts/<int:post_pk>/", PostsRetrieveView.as_view(), name="retrieve-post"),
    path("posts/<int:post_pk>/delete/", PostsDeleteView.as_view(), name="delete-post"),
    # Comments
    path(
        "posts/<int:post_pk>/comments/",
        CommentsListsPostView.as_view(),
        name="list-post-comments",
    ),
    path(
        "posts/<int:post_pk>/comments/create/",
        CommentsCreateView.as_view(),
        name="create-comment",
    ),
    path(
        "posts/<int:post_pk>/comments/<int:comment_pk>/",
        CommentsRetrieveView.as_view(),
        name="retrieve-comment",
    ),
    path(
        "posts/<int:post_pk>/comments/<int:comment_pk>/delete/",
        CommentsDeleteView.as_view(),
        name="delete-comment",
    ),
    # Likes
    path(
        "posts/<int:post_pk>/likes/",
        LikesPostView.as_view(),
        name="likes-post",
    ),
]
