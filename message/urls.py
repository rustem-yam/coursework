from django.urls import path
from . import views

app_name = "message"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:user_pk>/", views.chat, name="chat"),
    path("<int:user_pk>/send", views.send, name="send"),
]
