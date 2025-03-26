from ..models import Currency


class CurrencyRepository:
    @staticmethod
    def create(cur_data):
        currency = Currency(
            code=cur_data["code"],
            name=cur_data["name"],
        )
        currency.save()
        return currency

    @staticmethod
    def get_all():
        return Currency.objects.all()

    @staticmethod
    def get_by_id(pk):
        return Currency.objects.get(id=pk)
