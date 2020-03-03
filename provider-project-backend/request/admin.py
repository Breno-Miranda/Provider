from django.contrib import admin
from .models import Request , Itens , Status


admin.site.empty_value_display = '(empty)'


class BindAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'type', 'team', 'sector', 'user_link', 'is_active')

admin.site.register(Request)
admin.site.register(Itens)
admin.site.register(Status)
