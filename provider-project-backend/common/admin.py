from django.contrib import admin
from .models import Catalog, Zone, Provider

admin.site.register(Provider)
admin.site.register(Catalog)
admin.site.register(Zone)
