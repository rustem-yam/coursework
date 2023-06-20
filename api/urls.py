from django.urls import path
from .views import (
    CreatePostView,
    ListPostsView,
    RetrievePostView,
    DeletePostView,
    ListPostCommentsView,
    RetrieveCommentView,
    CreateCommentView,
    DeleteCommentView,
    LikesPostView,
)

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Posts
    path("posts/create/", CreatePostView.as_view(), name="create-post"),
    path("posts/", ListPostsView.as_view(), name="list-posts"),
    path("posts/<int:post_pk>/", RetrievePostView.as_view(), name="retrieve-post"),
    path("posts/<int:post_pk>/delete/", DeletePostView.as_view(), name="delete-post"),
    # Comments
    path(
        "posts/<int:post_pk>/comments/",
        ListPostCommentsView.as_view(),
        name="list-post-comments",
    ),
    path(
        "posts/<int:post_pk>/comments/create/",
        CreateCommentView.as_view(),
        name="create-comment",
    ),
    path(
        "posts/<int:post_pk>/comments/<int:comment_pk>/",
        RetrieveCommentView.as_view(),
        name="retrieve-comment",
    ),
    path(
        "posts/<int:post_pk>/comments/<int:comment_pk>/delete/",
        DeleteCommentView.as_view(),
        name="delete-comment",
    ),
    # Likes
    path(
        "posts/<int:post_pk>/likes/",
        LikesPostView.as_view(),
        name="likes-post",
    ),
]
