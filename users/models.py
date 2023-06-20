from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    firstname = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    email = models.CharField(unique=True)
    password = models.CharField(max_length=255)
    registration_date = models.DateField(default="2000-01-01")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.firstname + "_" + self.lastname

    def get_username(self):
        return self.email
