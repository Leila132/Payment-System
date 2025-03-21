from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField(
        write_only=True, required=True, validators=[validate_email]
    )
    phone = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    country = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "phone",
            "first_name",
            "last_name",
            "country",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        if attrs["phone"].isdigit() == False:
            raise serializers.ValidationError(
                {"phone": "Телефон может содержать только цифры"}
            )
        if len(attrs["country"]) != 2:
            raise serializers.ValidationError(
                {
                    "country": "Страна должна быть в формате кода ISO и содержать только два символа"
                }
            )
        return attrs

    def create(self, validated_data):
        phone = validated_data.pop("phone")
        country = validated_data.pop("country")
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        UserProfile.objects.create(user=user, phone=phone, country=country)
        return user
