from django.contrib import admin
from .models import Company, Contact, Plan, Key, Catalog

admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Plan)
admin.site.register(Key)
admin.site.register(Catalog)
