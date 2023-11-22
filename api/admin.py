from django.contrib import admin
from import_export.admin import ExportMixin

# Register your models here.
from datetime import date
from .models import Post, Comment, Like
from .resources import PostResource, CommentResource


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class LikeInline(admin.TabularInline):
    model = Like
    extra = 1


class PostAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = PostResource

    fieldsets = [
        ("User Info", {"fields": ["user"]}),
        ("Date Info", {"fields": ["creation_date"]}),
        (None, {"fields": ["text"]}),
    ]
    date_hierarchy = "creation_date"
    inlines = [CommentInline, LikeInline]
    list_display = ["id", "user", "creation_date", "text"]
    list_filter = ["user", "creation_date", "text"]
    search_fields = [
        "text",
        "user__firstname",
        "user__lastname",
    ]

    def get_export_queryset(self, request):
        today = date.today()

        queryset = super().get_export_queryset(request)

        queryset = queryset.filter(creation_date__lte=today)

        return queryset


class CommentAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CommentResource
    list_display = ["id", "user", "post", "creation_date", "text"]
    date_hierarchy = "creation_date"
    list_filter = ["user", "post", "creation_date", "text"]
    search_fields = [
        "text",
        "user__firstname",
        "user__lastname",
        "post__text",
    ]


class LikeAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "post", "date_added"]
    date_hierarchy = "date_added"
    list_filter = ["user", "post", "date_added"]
    search_fields = [
        "post__text",
        "user__firstname",
        "user__lastname",
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
