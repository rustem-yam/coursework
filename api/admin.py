from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Like


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class LikeInline(admin.TabularInline):
    model = Like
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("User Info", {"fields": ["user"]}),
        ("Date Info", {"fields": ["creation_date"]}),
        (None, {"fields": ["text"]}),
    ]
    date_hierarchy = "creation_date"
    inlines = [CommentInline, LikeInline]
    list_display = ["id", "user", "creation_date", "text"]
    list_filter = ["user", "creation_date", "text"]
    search_fields = ["text"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "post", "creation_date", "text"]
    date_hierarchy = "creation_date"
    list_filter = ["user", "post", "creation_date", "text"]
    search_fields = ["text"]


class LikeAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "post", "date_added"]
    date_hierarchy = "date_added"
    list_filter = ["user", "post", "date_added"]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
