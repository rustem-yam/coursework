from django.contrib import admin
from message.models import Message


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Users Info", {"fields": ["sender", "recipient"]}),
        ("Date Info", {"fields": ["send_date"]}),
        (None, {"fields": ["text"]}),
    ]

    date_hierarchy = "send_date"

    list_display = [
        "id",
        "sender",
        "recipient",
        "send_date",
        "text",
        "was_sent_recently",
    ]

    list_filter = [
        "sender",
        "recipient",
        "send_date",
        "text",
    ]
    search_fields = [
        "text",
        "sender__firstname",
        "sender__lastname",
        "recipient__firstname",
        "recipient__firstname",
    ]

    raw_id_fields = [
        "sender",
        "recipient",
    ]


admin.site.register(Message, MessageAdmin)
