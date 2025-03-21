from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, UserSerializer


class AuthService:
    @staticmethod
    def register_user(data):
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return {
                "success": True,
                "token": token.key,
                "user": UserSerializer(user).data
            }, None
        return None, serializer.errors

    @staticmethod
    def login_user(username, password):
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return {
                "success": True,
                "token": token.key,
                "user": UserSerializer(user).data
            }, None
        return None, {"error": "Неверные учетные данные"}

    @staticmethod
    def verify_token(token_key):
        if not token_key:
            return None, {"error": "Token not provided"}
        
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
            return {
                "user_id": user.id,
                "username": user.username,
                "valid": True,
                "email": user.email,
                "phone": user.profile.phone,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "country": user.profile.country,
            }, None
        except Token.DoesNotExist:
            return None, {"valid": False}