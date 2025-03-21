from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .services import AuthService


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        result, error = AuthService.register_user(request.data)
        if result:
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        result, error = AuthService.login_user(username, password)
        if result:
            return Response(result)
        return Response(error, status=status.HTTP_401_UNAUTHORIZED)


class VerifyTokenAPI(APIView):
    def post(self, request):
        token_key = request.data.get("token")
        result, error = AuthService.verify_token(token_key)
        
        if result:
            return Response(result)
        if "valid" in error:
            return Response(error, status=404)
        return Response(error, status=400)