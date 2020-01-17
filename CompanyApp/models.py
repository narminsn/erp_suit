from django.db import models

# Create your models here.


class CompanyModel(models.Model):
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

    def azn_value(self):
        arr = self.account.all()
        val = 0
        for i in arr:
            val += i.azn_value()
        return val


class AccountsModel(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE,related_name='account')
    OFFİCİAL = 'RƏSMİ'
    UNOFFİCİAL = 'QEYRİ-RƏSMİ'

    type_choices = [
        (OFFİCİAL, 'Official'),
        (UNOFFİCİAL, 'Unofficial'),
    ]
    type = models.CharField(
        max_length=25,
        choices=type_choices,

    )
    AZN = "AZN"
    EUR = 'EUR'
    USD = 'USD'

    currency_choices = [
        (AZN, 'Azn'),
        (EUR, 'Eur'),
        (USD, 'Usd')
    ]
    currency = models.CharField(
        max_length=4,
        choices=currency_choices
    )



    def __str__(self):
        return self.name

    # def value(self):
    #     arr = self.transactions.all()
    #     val = 0
    #     for i in arr:
    #         val+=i.value
    #     return val
    #
    # def azn_value(self):
    #     arr = self.transactions.all()
    #     val = 0
    #     for i in arr:
    #         val += i.azn_value
    #
    #     return round(val,2)
    #


