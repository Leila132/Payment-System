from django.urls import path
from .views import RegisterAPIView, LoginAPIView, VerifyTokenAPI

urlpatterns = [
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),
    path('api/login/', LoginAPIView.as_view(), name='api_login'),
    path('api/verify-token/', VerifyTokenAPI.as_view(), name='verify-token'),
]