from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # USD, EUR, RUB
    name = models.CharField(max_length=50)  # Доллар США, Евро, Рубль

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class Payment(models.Model):
    user_id = models.UUIDField()
    product = models.CharField("Продукт", max_length=100)
    amount = models.DecimalField("Сумма", max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    token = models.CharField("Токен платежа", max_length=100)
    status = models.CharField(
        "Статус",
        max_length=100,
        choices=[
            ("Создан", "Создан"),
            ("Подтвержден", "Подтвержден"),
            ("Отклонен", "Отклонен"),
            ("Завершен", "Завершен"),
        ],
        default="Создан",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
