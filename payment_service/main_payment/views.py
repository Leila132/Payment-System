from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.response import Response
import requests
from django.http import HttpResponseRedirect, HttpResponse
import requests
import json
from .services import get_user_from_token, create_payment
from .serializers import PaymentSerializer
from rest_framework import status

class createPaymentAPI(APIView):
    def post(self, request: Request) -> Response:
        payment_data = request.data.copy()
        user = get_user_from_token(payment_data.get("token"))
        if not user:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = PaymentSerializer(data=payment_data)
        if not serializer.is_valid():
            return Response({
                "error": "Неверные данные",
                "details": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        payment = serializer.save() 
        return Response({
            "message": "Платеж успешно создан",
            "payment_id": payment.id,
            "product": payment.product,
            "amount": payment.amount,
            "currency": payment.currency
        }, status=status.HTTP_201_CREATED)
        
