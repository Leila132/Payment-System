from django.urls import path
from .views import createPaymentAPI

urlpatterns = [
    path('create_payment/', createPaymentAPI.as_view(), name='create')
]