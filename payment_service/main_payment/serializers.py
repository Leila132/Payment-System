from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["product", "amount", "currency"]

    def validate(self, data):
        # Проверка наличия всех обязательных полей
        required_fields = ["product", "amount", "currency"]
        for field in required_fields:
            if field not in data:
                raise serializers.ValidationError({field: "Это поле обязательно."})
        return data

    def validate_amount(self, value):
        """
        Проверка, что сумма больше нуля.
        """
        if value <= 0:
            raise serializers.ValidationError("Сумма должна быть больше нуля.")
        return value
