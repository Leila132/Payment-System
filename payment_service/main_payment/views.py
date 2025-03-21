from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import PaymentSerializer
from .services.user_service import UserService
from .services.payment_service import PaymentService


class CreatePaymentAPI(APIView):
    def post(self, request: Request) -> Response:
        payment_data = request.data.copy()
        user = UserService.get_user_from_token(payment_data.get("token"))

        if not user:
            return Response(
                {"error": "Пользователь не найден"}, status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = PaymentSerializer(data=payment_data)
        if not serializer.is_valid():
            return Response(
                {"error": "Неверные данные", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        response = PaymentService.create_payment(payment_data, user)
        return Response(response, status=status.HTTP_201_CREATED)


class PaymentsAPI(APIView):
    def get(self, request: Request) -> Response:
        payment_data = request.data.copy()
        user = UserService.get_user_from_token(payment_data.get("token"))

        if not user:
            return Response(
                {"error": "Пользователь не найден"}, status=status.HTTP_401_UNAUTHORIZED
            )

        result = PaymentService.get_payments_list(payment_data, user)

        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result)
    
class ConfirmPaymentAPI(APIView):
    def post(self, request: Request) -> Response:
        payment_data = request.data.copy()
        user = UserService.get_user_from_token(payment_data.get("user_token"))

        if not user:
            return Response(
                {"error": "Пользователь не найден"}, status=status.HTTP_401_UNAUTHORIZED
            )

        result = PaymentService.confirm_payment(payment_data, user)

        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        return Response(result)
