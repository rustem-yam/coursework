from django.urls import path
from .views import CreatePostView, ListPostsView, RetrievePostView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/create/", CreatePostView.as_view(), name="create-post"),
    path("post/", ListPostsView.as_view(), name="list-posts"),
    path("post/<int:pk>/", RetrievePostView.as_view(), name="retrieve-post"),
]
