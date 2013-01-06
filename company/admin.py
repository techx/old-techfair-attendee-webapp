from company.models import Company
from django.contrib import admin

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('Company_Display_Name','Company_Description')

admin.site.register(Company, CompanyAdmin)
