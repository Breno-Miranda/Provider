from django.contrib import admin
from .models import Company, Contact, Plan, Key, Catalog


admin.site.register(Contact)
admin.site.register(Plan)
admin.site.register(Key)
admin.site.register(Catalog)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name_company', 'cnpj', 'date_register', 'is_active')

admin.site.register(Company, CompanyAdmin)
