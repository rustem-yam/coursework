from django.urls import path
from .views import (
    RegisterUserView,
    LoginUserView,
    LogoutUserView,
    ListUsersView,
    RetrieveUserView,
    FriendUserView,
    UnfriendUserView,
)

urlpatterns = [
    path("", ListUsersView.as_view(), name="list-users"),
    path("<int:user_pk>/", RetrieveUserView.as_view(), name="retrieve-user"),
    path("<int:user_pk>/friend", FriendUserView.as_view(), name="friend-user"),
    path("<int:user_pk>/unfriend", UnfriendUserView.as_view(), name="unfriend-user"),
    path("register", RegisterUserView.as_view(), name="register"),
    path("login", LoginUserView.as_view(), name="login"),
    path("logout", LogoutUserView.as_view(), name="logout"),
]
