from django.contrib import admin

# Register your models here.
from .models import Request , Itens , Status


admin.site.register(Request)
admin.site.register(Itens)
admin.site.register(Status)