from django.contrib import admin
from .models import Request , Itens , Status


admin.site.empty_value_display = '(empty)'


class RequestAdmin(admin.ModelAdmin):
    list_display = ('profile', 'company', 'campaign', 'lot', 'catalog', 'amount', 'status', 'create_date')

class ItensAdmin(admin.ModelAdmin):
    list_display = ('product', 'request', 'amount', 'total', 'is_checked')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('type', 'company', 'initials', 'code', 'description', 'is_active')

admin.site.register(Request, RequestAdmin)
admin.site.register(Itens, ItensAdmin)
admin.site.register(Status, StatusAdmin)
