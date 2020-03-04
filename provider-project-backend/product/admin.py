from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Product, Category, Color, Gallery, Status

admin.site.empty_value_display = '(empty)'

class ProductAdmin(ImportExportModelAdmin):
    list_display = ('description', 'reference', 'amount', 'sale_price', 'page', 'value_provider', 'stock', 'catalog')



admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Gallery)
admin.site.register(Status)
admin.site.register(Product, ProductAdmin)
