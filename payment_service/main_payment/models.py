from django.db import models

class Payment(models.Model):
    product = models.CharField('Продукт', max_length=100)
    amount = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    currency = models.CharField('Валюта', max_length=3, choices=[
        ('NGN', 'NGN'),
        ('GHS', 'GHS')
    ], default='NGN')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'