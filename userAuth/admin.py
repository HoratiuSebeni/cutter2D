from django.contrib import admin
from .models import Company, CompanyEmployer

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company', 'companyType')

class CompanyEmployerAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'accountPermisions')

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyEmployer, CompanyEmployerAdmin)
