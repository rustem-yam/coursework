from django.contrib import admin
from .models import CustomUser, Friend, Message
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "firstname",
        "lastname",
        "password",
        "registration_date",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "firstname",
        "lastname",
        "password",
        "registration_date",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "firstname",
                    "lastname",
                    "password",
                    "registration_date",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = (
        "firstname",
        "lastname",
        "password",
        "registration_date",
    )
    ordering = (
        "firstname",
        "lastname",
        "password",
        "registration_date",
    )


# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Message)
admin.site.register(Friend)
