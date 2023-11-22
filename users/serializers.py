from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "firstname",
            "lastname",
            "email",
            "password",
        )


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=254)

    def validate_firstname(self, firstname):
        if len(firstname) > 20:
            raise serializers.ValidationError(
                "У вас слишком длинное имя. Введите покороче или смените в ЗАГСе"
            )

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "firstname",
            "lastname",
            "password",
        )


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=254)

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password",
        )


class PublicUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "firstname",
            "lastname",
            "registration_date",
        )
