from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Message, Like, Friend

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Like)
admin.site.register(Friend)