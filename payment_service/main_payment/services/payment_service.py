import json
import requests
from django.http import HttpResponse
from django.conf import settings
from dotenv import dotenv_values
from ..repositories.payment_repository import PaymentRepository
from ..utils.validators import check_date

config = dotenv_values()


class PaymentService:
    @staticmethod
    def create_payment(payment_data, user):
        # Сохраняем в БД
        payment = PaymentRepository.create(payment_data)

        # Отправляем запрос во внешний API
        MERCHANT_PRIVATE_KEY = config["API_TOKEN"]
        SANDBOX_URL = config["SANDBOX_URL"]

        payload = {
            "product": payment_data["product"],
            "amount": payment_data["amount"],
            "currency": payment_data["currency"],
            "customer": {
                "email": user["email"],
                "phone": user["phone"],
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "country": user["country"],
            },
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {MERCHANT_PRIVATE_KEY}",
        }

        resp = requests.post(
            f"{SANDBOX_URL}/api/v1/payments", json=payload, headers=headers
        )

        if resp.status_code == 200:
            response_data = json.loads(resp.text)
            return {
                "token": response_data.get("token"),
                "processingUrl": response_data.get("processingUrl"),
            }
        else:
            return {"error": f"API error: {resp.status_code}", "details": resp.text}

    @staticmethod
    def get_payments_list(payment_data, user):
        if not check_date(payment_data.get("date_start")) or not check_date(
            payment_data.get("date_end")
        ):
            return {"error": "Invalid date format"}

        MERCHANT_PRIVATE_KEY = user["user_token_api"]
        SANDBOX_URL = config["SANDBOX_URL"]

        params = {
            "dateFrom": payment_data["date_start"],
            "dateTo": payment_data["date_end"],
            "page": 1,
            "perPage": 20,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {MERCHANT_PRIVATE_KEY}",
        }

        resp = requests.get(
            f"{SANDBOX_URL}/api/v1/payments", params=params, headers=headers
        )

        if resp.status_code == 200:
            return json.loads(resp.text)
        else:
            return {"error": f"API error: {resp.status_code}", "details": resp.text}
