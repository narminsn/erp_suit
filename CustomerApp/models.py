from django.db import models
from datetime import  date
# Create your models here.


class CustomerModel(models.Model):
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.customer_name

    def projects_num(self):
        return len(self.projects.all())

    def azn_value(self):
        arr = self.transactions.all()
        val = 0
        for i in arr:
            val += i.azn_value
        return val



class PersonsModel(models.Model):
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    full_name = models.CharField(max_length=255, default='')
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE,related_name='persons')
    phone = models.CharField(max_length=125)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.full_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.full_name = f'{self.first_name} {self.last_name}'

        return super(PersonsModel, self).save()

    def projects_num(self):
        return len(self.projects.all())
    #
    # def azn_value(self):
    #     arr = self.transactions.all()
    #     val = 0
    #     for i in arr:
    #         val += i.azn_value
    #     return val


class ProjectsModel(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(CustomerModel,on_delete=models.CASCADE, related_name='projects')

    person = models.ForeignKey(PersonsModel,
                               on_delete=models.CASCADE,related_name='projects'
                               )

    date = models.DateField(default=date.today())

    def __str__(self):
        return self.name

