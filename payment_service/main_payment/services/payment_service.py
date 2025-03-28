import json
import requests
from django.http import HttpResponse
from django.conf import settings
from dotenv import dotenv_values
from ..repositories.payment_repository import PaymentRepository
from ..utils.validators import check_date
from ..repositories.currency_repository import CurrencyRepository

config = dotenv_values()


class PaymentService:
    @staticmethod
    def create_payment(payment_data, user):
        # Сохраняем в БД
        currency = CurrencyRepository.get_by_id(payment_data["currency"])
        payment = PaymentRepository.create(payment_data, user, currency)

        # Отправляем запрос во внешний API
        MERCHANT_PRIVATE_KEY = config["API_TOKEN"]
        SANDBOX_URL = config["SANDBOX_URL"]
        URL = config["PAYMENTS_URL"]
        payload = {
            "product": payment_data["product"],
            "amount": payment_data["amount"],
            "currency": currency.code,
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

        resp = requests.post(f"{SANDBOX_URL}{URL}", json=payload, headers=headers)

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

        MERCHANT_PRIVATE_KEY = config["API_TOKEN"]
        SANDBOX_URL = config["SANDBOX_URL"]
        URL = config["PAYMENTS_URL"]

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

        resp = requests.get(f"{SANDBOX_URL}{URL}", params=params, headers=headers)

        if resp.status_code == 200:
            return json.loads(resp.text)
        else:
            return {"error": f"API error: {resp.status_code}", "details": resp.text}

    @staticmethod
    def confirm_payment(payment_data, user):
        MERCHANT_PRIVATE_KEY = config["API_TOKEN"]
        SANDBOX_URL = config["SANDBOX_URL"]
        URL = config["CONFIRM_URL"]

        params = {
            "token": payment_data["token"],
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {MERCHANT_PRIVATE_KEY}",
        }

        resp = requests.get(f"{SANDBOX_URL}{URL}", params=params, headers=headers)

        if resp.status_code == 200:
            update_payment = PaymentRepository.change_status(
                payment_data["id"], "Подтвержден"
            )
            return json.loads(resp.text)
        else:
            return {"error": f"API error: {resp.status_code}", "details": resp.text}

    @staticmethod
    def decline_payment(payment_data, user):
        MERCHANT_PRIVATE_KEY = config["API_TOKEN"]
        SANDBOX_URL = config["SANDBOX_URL"]
        URL = config["DECLINE_URL"]

        params = {
            "token": payment_data["token"],
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {MERCHANT_PRIVATE_KEY}",
        }

        resp = requests.get(f"{SANDBOX_URL}{URL}", params=params, headers=headers)

        if resp.status_code == 200:
            update_payment = PaymentRepository.change_status(
                payment_data["id"], "Отклонен"
            )
            return json.loads(resp.text)
        else:
            return {"error": f"API error: {resp.status_code}", "details": resp.text}

    @staticmethod
    def create_currency(cur_data):
        # Сохраняем в БД
        currency = CurrencyRepository.create(cur_data)
        return currency
