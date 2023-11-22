from import_export import resources
from datetime import datetime, timedelta
from import_export.fields import Field
import logging

from .models import Post, Comment


class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ("id", "user", "text", "creation_date")


class CommentResource(resources.ModelResource):
    full_title = Field()

    class Meta:
        model = Comment
        fields = ("id", "post", "user", "text", "creation_date")

    def dehydrate_full_title(self, comment):
        author = getattr(comment.user, "firstname", "unknown")
        post = getattr(comment.post, "id", "unknown")
        return "%s commented post %s" % (author, post)

    def after_export(self, queryset, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info("Data export from table Comments successfully completed")
