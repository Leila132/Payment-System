from django.db import models


class Payment(models.Model):
    product = models.CharField("Продукт", max_length=100)
    amount = models.DecimalField("Сумма", max_digits=10, decimal_places=2)
    currency = models.CharField(
        "Валюта", max_length=3, choices=[("NGN", "NGN"), ("GHS", "GHS")], default="NGN"
    )
    token = models.CharField("Токен платежа", max_length=100)
    status = models.CharField(
        "Статус", max_length=100, choices=[("Создан", "Создан"), ("Подтвержден", "Подтвержден"), ("Отклонен", "Отклонен"), ("Завершен", "Завершен")], default="Создан"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
