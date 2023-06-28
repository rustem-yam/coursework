from django.urls import reverse
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from users.models import CustomUser
from .models import Message
from django.db.models import Q
from django.utils import timezone
import datetime


# Create your views here.
def index(request):
    return HttpResponse(
        "Hello, you are at messages index. If you want to see messages for exact user, you have to add to the current URL that users' id and be authorized."
    )


def chat(request, user_pk):
    if not request.user.is_authenticated:
        login_url = reverse(settings.LOGIN_URL)
        return redirect(login_url)

    user_1 = request.user

    try:
        user_2 = CustomUser.objects.get(pk=user_pk)
    except CustomUser.DoesNotExist:
        return HttpResponse("Error! User not found.")

    messages = Message.objects.filter(
        Q(sender=user_1, recipient=user_2) | Q(sender=user_2, recipient=user_1)
    ).order_by("send_date")

    context = {
        "messages": messages,
        "user_1": user_1,
        "user_2": user_2,
    }

    return render(request, "message/chat.html", context)


def send(request, user_pk):
    if not request.user.is_authenticated:
        login_url = reverse(settings.LOGIN_URL)
        return redirect(login_url)

    user_1 = request.user
    user_2 = get_object_or_404(CustomUser, pk=user_pk)

    text = request.POST["text"]

    message = Message(
        sender=user_1, recipient=user_2, text=text, send_date=timezone.now()
    )
    message.save()

    return HttpResponseRedirect(reverse("message:chat", args=(user_pk,)))
