from django.contrib import admin
from .models import Catalog, Zone, Provider, Payment_methods

admin.site.empty_value_display = '(empty)'


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('provider', 'name', 'commission', 'zone', 'create_date', 'last_date', 'is_active')

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'cnpj', 'social_name', 'fancy_name', 'date_register')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('type', 'number', 'initials', 'description', 'is_active')

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'initials')


admin.site.register(Provider, ProviderAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Zone, ZoneAdmin)
admin.site.register(Payment_methods, PaymentAdmin)
