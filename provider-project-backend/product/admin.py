from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Product, Category, Color, Gallery, Status


admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Gallery)
admin.site.register(Status)

class ProductAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
