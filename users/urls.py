from django.urls import path
from .views import (
    UsersRegisterView,
    UsersLoginView,
    UsersLogoutView,
    UsersListView,
    UsersRetrieveView,
    UsersFriendView,
    UsersUnfriendView,
)

urlpatterns = [
    path("", UsersListView.as_view(), name="list-users"),
    path("<int:user_pk>/", UsersRetrieveView.as_view(), name="retrieve-user"),
    path("<int:user_pk>/friend", UsersFriendView.as_view(), name="friend-user"),
    path("<int:user_pk>/unfriend", UsersUnfriendView.as_view(), name="unfriend-user"),
    path("register", UsersRegisterView.as_view(), name="register"),
    path("login", UsersLoginView.as_view(), name="login"),
    path("logout", UsersLogoutView.as_view(), name="logout"),
]
