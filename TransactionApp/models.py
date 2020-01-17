from django.db import models
from datetime import date

from CustomerApp.models import CustomerModel, PersonsModel, ProjectsModel
from CompanyApp.models import CompanyModel, AccountsModel
# Create your models here.


class AssignmentModel(models.Model):
    name = models.CharField(max_length=255)
    assignment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                   limit_choices_to={'parent': True}
                                   )
    parent = models.BooleanField(default=False)


    def __str__(self):
        return self.name


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.assignment:
            self.parent = True
        return super(AssignmentModel, self).save()

    def azn_value(self):
        arr = self.transactions.all()
        val = 0
        for i in arr:
            val += i.azn_value
        return val





class TransactionModel(models.Model):
    currency_choices = [
        ('Expense', 'expense'),
        ('Revenue', 'revenue'),
        ('Debt', 'debt'),
    ]
    type = models.CharField(max_length=10,choices=currency_choices)
    date = models.DateField(default=date.today())
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='transactions')
    person = models.ForeignKey(PersonsModel, on_delete=models.CASCADE, related_name='transactions')
    project = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE)
    assignment = models.ForeignKey(AssignmentModel, on_delete=models.CASCADE,
                                   related_name='transactions',
                                   limit_choices_to={'parent': False}
                                   )
    account =  models.ForeignKey(AccountsModel, on_delete=models.CASCADE,
                                 related_name='transactions')
    AZN = "AZN"
    EUR = 'EUR'
    USD = 'USD'

    currency_choices = [
        (AZN, 'AZN'),
        (EUR, 'EUR'),
        (USD, 'USD')
    ]
    currency = models.CharField(
        max_length=4,
        choices=currency_choices
    )
    value = models.FloatField()
    azn_value = models.FloatField(default=0)


    # def save(self, force_insert=False, force_update=False, using=None,
        #      update_fields=None):
        #
        #
        #
        # if self.type == 'Expense':
        #     self.value = 0-self.value
        #
        # azn_value = exchange(self.value, self.currency)
        # self.azn_value = azn_value
        # return super(TransactionModel, self).save()

