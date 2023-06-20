from rest_framework import status, generics
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
