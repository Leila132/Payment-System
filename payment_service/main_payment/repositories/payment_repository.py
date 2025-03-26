from ..models import Payment


class PaymentRepository:
    @staticmethod
    def create(payment_data, user, currency):
        print(payment_data)
        payment = Payment(
            product=payment_data["product"],
            amount=payment_data["amount"],
            currency=currency,
            user_id=user["user_id"],
        )
        payment.save()
        return payment

    @staticmethod
    def get_all():
        return Payment.objects.all()

    @staticmethod
    def change_status(pk, status):
        return Payment.objects.get(id=pk).update(status=status)
