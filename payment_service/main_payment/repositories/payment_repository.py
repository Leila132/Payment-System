from ..models import Payment

class PaymentRepository:
    @staticmethod
    def create(payment_data):
        payment = Payment(
            product=payment_data['product'],
            amount=payment_data['amount'],
            currency=payment_data['currency']
        )
        payment.save()
        return payment
    
    @staticmethod
    def get_all():
        return Payment.objects.all()