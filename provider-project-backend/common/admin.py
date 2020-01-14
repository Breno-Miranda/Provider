from django.contrib import admin
from .models import Catalog, Zone, Provider, Payment_methods

admin.site.register(Provider)
admin.site.register(Catalog)
admin.site.register(Zone)
admin.site.register(Payment_methods)
