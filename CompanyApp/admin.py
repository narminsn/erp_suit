from django.contrib import admin
from django.utils.html import format_html
# from import_export.admin import ImportExportModelAdmin
# from import_export.formats import base_formats
from . import models
#
#
# # Register your models here.

# class Accountinline(admin.StackedInline):
#     model = models.AccountsModel
#     extra = 1
#
# class Personsline(admin.StackedInline):
#     model = models.PersonsModel
#     extra = 1
#
#
# #
@admin.register(models.CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/companymodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/companymodel/{}/delete/">Delete</a>', obj.id)

    # inlines = [Accountinline]
    list_display = ['company_name', 'azn_value', 'ACTIONS','ACTION' ]
    exclude = ['value']
    list_per_page = 5





@admin.register(models.AccountsModel)
class CompanyAdmin(admin.ModelAdmin):
    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/accountsmodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/accountsmodel/{}/delete/">Delete</a>', obj.id)

    list_display = ['name', 'company', 'currency',  'ACTIONS','ACTION' ]
    list_per_page = 5
    exclude = ['azn_val']



# # admin.site.register(models.TransactionModel)
#
