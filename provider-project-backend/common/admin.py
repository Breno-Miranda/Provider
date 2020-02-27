from django.contrib import admin
from .models import Catalog, Zone, Provider, Payment_methods

admin.site.empty_value_display = '(empty)'

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('provider', 'name', 'commission', 'zone', 'create_date', 'last_date', 'is_active')

admin.site.register(Provider)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Zone)
admin.site.register(Payment_methods)
