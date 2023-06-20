from rest_framework.views import APIView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from rest_framework import status, generics
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import login, authenticate, logout

# from django.shortcuts import redirect
from .serializers import (
    UserSerializer,
    RegisterUserSerializer,
    LoginUserSerializer,
    PublicUserSerializer,
)
from .models import CustomUser, Friend, Message
from rest_framework.response import Response
import json
from datetime import date


# Create your views here.
class RegisterUserView(APIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if not (serializer.is_valid()):
            return Response(
                {"Bad Request": "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST
            )

        email = serializer.data.get("email")
        firstname = serializer.data.get("firstname")
        lastname = serializer.data.get("lastname")
        password = serializer.data.get("password")
        registration_date = date.today()

        emails = [
            self.serializer_class(user).data["email"]
            for user in CustomUser.objects.all()
        ]

        if email in emails:
            return Response(
                {"Reg Error": "Email is not unique"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = CustomUser.objects.create_user(
            email=email,
            firstname=firstname,
            lastname=lastname,
            password=password,
            registration_date=registration_date,
        )

        login(request, user)

        return Response(
            self.serializer_class(user).data, status=status.HTTP_201_CREATED
        )


class LoginUserView(APIView):
    serializer_class = LoginUserSerializer

    def post(self, request, format=None):
        if request.user.is_authenticated:
            return Response(
                {"Login Error": f"User {request.user} is already logged in"},
                status=status.HTTP_423_LOCKED,
            )
        serializer = self.serializer_class(data=request.data)
        if not (serializer.is_valid()):
            return Response(
                {
                    "Bad Request": "Invalid data...",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        email = serializer.data.get("email")
        password = serializer.data.get("password")

        user = CustomUser.objects.authenticate(request, email=email, password=password)
        if user is None:
            return Response(
                {"Login Error": f"Invalid email or password {user}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        login(request, user)
        return Response(
            {"Login Successfully": f"{user}"}, status=status.HTTP_202_ACCEPTED
        )


class LogoutUserView(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response({"Logout successfully"}, status=status.HTTP_200_OK)


class ListUsersView(APIView):
    serializer_class = PublicUserSerializer

    def get(self, request, format=None):
        limit = request.query_params.get("limit") or 10
        page = request.query_params.get("page") or 1

        users = CustomUser.objects.all().order_by("id")

        paginator = Paginator(users, limit)

        try:
            users_page = paginator.page(page)
        except Exception as e:
            return Response(
                {"Bad Request": "Invalid page number"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(users_page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveUserView(APIView):
    serializer_class = PublicUserSerializer

    def get(self, request, user_pk, format=None):
        try:
            user = CustomUser.objects.get(pk=user_pk)
        except CustomUser.DoesNotExist:
            return Response(
                {"Not Found": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FriendUserView(APIView):
    def post(self, request, user_pk, format=None):
        if not request.user.is_authenticated:
            login_url = reverse(settings.LOGIN_URL)
            return redirect(login_url)
        user_1 = request.user

        try:
            user_2 = CustomUser.objects.get(pk=user_pk)
        except CustomUser.DoesNotExist:
            return Response(
                {"Not Found": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if user_1.id == user_2.id:
            return Response(
                {"Error": "You cannot add yourself to friends"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            friendship = Friend.objects.get(user_1=user_1, user_2=user_2)
            return Response(
                {"Error": "User is already a friend"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Friend.DoesNotExist:
            pass

        date_added = date.today()

        friend = Friend(user_1=user_1, user_2=user_2, date_added=date_added)

        friend.save()
        return Response(
            f"{user_1} added {user_2} to friends", status=status.HTTP_201_CREATED
        )


class UnfriendUserView(APIView):
    def post(self, request, user_pk, format=None):
        if not request.user.is_authenticated:
            login_url = reverse(settings.LOGIN_URL)
            return redirect(login_url)
        user_1 = request.user

        try:
            user_2 = CustomUser.objects.get(pk=user_pk)
        except CustomUser.DoesNotExist:
            return Response(
                {"Not Found": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if user_1.id == user_2.id:
            return Response(
                {"Error": "You cannot delete yourself from friends"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            friendship = Friend.objects.get(user_1=user_1, user_2=user_2)
        except Friend.DoesNotExist:
            return Response(
                {"Error": "User is not a friend"}, status=status.HTTP_400_BAD_REQUEST
            )

        friendship.delete()
        return Response(
            f"{user_1} deleted {user_2} from friends", status=status.HTTP_202_ACCEPTED
        )
