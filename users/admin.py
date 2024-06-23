from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Friend, Visit
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "id",
        "email",
        "firstname",
        "lastname",
        "password",
        "registration_date",
        "is_staff",
        "is_active",
    )
    date_hierarchy = "registration_date"
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

    def save_model(self, request, obj, form, change):
        obj.username = obj.email  # Set the username as the email
        super().save_model(request, obj, form, change)


class FriendAdmin(admin.ModelAdmin):
    list_display = ["user_1", "user_2", "date_added"]
    date_hierarchy = "date_added"


class VisitAdmin(admin.ModelAdmin):
    list_display = ["user", "visit_date", "request_info"]


# Register your models here.

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Visit, VisitAdmin)
