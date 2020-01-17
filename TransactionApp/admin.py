from django.contrib import admin
from django.utils.html import format_html
from . import  models

# Register your models here.

@admin.register(models.AssignmentModel)
class AssignmentAdmin(admin.ModelAdmin):

    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/projectsmodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/projectsmodel/{}/delete/">Delete</a>', obj.id)


    list_display = ['name','azn_value',  'ACTIONS', 'ACTION']
    exclude = ['parent']




@admin.register(models.TransactionModel)
class TransactionAdmin(admin.ModelAdmin):
    # def get_export_formats(self):
    #
    #     formats = (
    #         base_formats.CSV,
    #
    #     )
    #     return [f for f in formats if f().can_export()]
    #
    # def get_import_formats(self):
    #
    #     formats = (
    #         base_formats.CSV,
    #
    #     )
    #     return [f for f in formats if f().can_export()]

    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/transactionmodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/transactionmodel/{}/delete/">Delete</a>', obj.id)

    def Value(self, obj):
        color = 'red'
        if obj.type == 'Expense' :
            color = 'red'
            return format_html('<b style="color:{};"> {}</b>',
            color,obj.value
            )
        else:
            color = 'green'
            return format_html('<b style="color:{};">+ {}</b>',
                               color, obj.value
                               )

    Value.admin_order_field = 'closed'

    list_display = ['date', 'company', 'customer','person', 'assignment' , 'account',  'Value', 'currency', 'ACTIONS', 'ACTION']
    list_filter = ['date', 'customer', 'customer','person','account']
    ordering = ('date',)
    list_per_page = 5
    exclude = ['azn_value']
