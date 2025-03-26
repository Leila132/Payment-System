from django.urls import path
from .views import (
    CreatePaymentAPI,
    PaymentsAPI,
    ConfirmPaymentAPI,
    DeclinePaymentAPI,
    CreateCurrencyAPI,
)

urlpatterns = [
    path("api/create_payment/", CreatePaymentAPI.as_view(), name="create"),
    path("api/payments/", PaymentsAPI.as_view(), name="payments_list"),
    path("api/confirm_payment/", ConfirmPaymentAPI.as_view(), name="confirm"),
    path("api/decline_payment/", DeclinePaymentAPI.as_view(), name="decline"),
    path("api/create_currency/", CreateCurrencyAPI.as_view(), name="create_cur"),
]
