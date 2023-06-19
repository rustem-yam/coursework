from django.contrib.auth.models import BaseUserManager
from datetime import date


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        email,
        firstname,
        password,
        lastname="",
        registration_date=date.today(),
        **extra_fields
    ):
        if not email:
            return ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            registration_date=registration_date,
            password=password,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, firstname="admin", **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(firstname, email, password, **extra_fields)
