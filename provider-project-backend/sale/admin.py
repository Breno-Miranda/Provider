from django.contrib import admin
from .models import Accrediting, Flags_card, Nature_operation, Payment_form, Sale, Status


admin.site.register(Accrediting)
admin.site.register(Flags_card)
admin.site.register(Nature_operation)
admin.site.register(Sale)
admin.site.register(Payment_form)
admin.site.register(Status)