from company.models import Company
from django.contrib import admin

class CompanyAdmin(admin.ModelAdmin):
    fields = ['Company_Display_Name']

admin.site.register(Company, CompanyAdmin)
