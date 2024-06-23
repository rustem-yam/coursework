from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname"]

    firstname = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    email = models.CharField(unique=True)
    password = models.CharField(max_length=255)
    registration_date = models.DateField(default="2000-01-01")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    def get_username(self):
        return self.email

    def get_id(self):
        return self.id

    def __str__(self):
        return str(self.firstname) + " " + str(self.lastname)


class Friend(models.Model):
    user_1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_1_friends"
    )
    user_2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_2_friends"
    )
    date_added = models.DateField()

    def __str__(self):
        return str(self.user_1) + " " + str(self.user_2)


class Visit(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(auto_now_add=True)
    request_info = models.TextField()

    def __str__(self):
        return f"{self.visit_date} {self.user} | {self.request_info}"
