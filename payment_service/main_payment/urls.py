from django.urls import path
from .views import createPaymentAPI, PaymentsAPI

urlpatterns = [
    path('api/create_payment/', createPaymentAPI.as_view(), name='create'),
    path('api/payments/', PaymentsAPI.as_view(), name='payments_list'),
]