from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    email = models.EmailField(unique=True, default="test@test.test")
    password = models.CharField(max_length=255)
    registration_date = models.DateField(default="2000-01-01")
    objects = CustomUserManager()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname + "_" + self.lastname
