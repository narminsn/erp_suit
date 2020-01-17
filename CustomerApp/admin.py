from django.contrib import admin
from django.utils.html import format_html
from . import  models
# Register your models here.

@admin.register(models.CustomerModel)
class CustomerAdmin(admin.ModelAdmin):




    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/customermodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/customermodel/{}/delete/">Delete</a>', obj.id)


@admin.register(models.PersonsModel)
class PersonsAdmin(admin.ModelAdmin):

    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/personsmodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/personsmodel/{}/delete/">Delete</a>', obj.id)

    exclude = ['full_name']
    list_display = ['full_name', 'customer','projects_num','ACTIONS','ACTION' ]
    list_per_page = 5


@admin.register(models.ProjectsModel)
class ProjectAdmin(admin.ModelAdmin):

    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/projectsmodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/projectsmodel/{}/delete/">Delete</a>', obj.id)

    list_display = ['name', 'customer',  'person', 'date','ACTIONS','ACTION']
    widget = ['make_published']
    exclude = ['ex_person', 'ex_customer']
    list_per_page = 5







#




