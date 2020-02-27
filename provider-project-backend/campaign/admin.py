from django.contrib import admin
from .models import Campaign

def date_convert(Campaign):
    return ("%s  - %s" % (Campaign.order_date.strftime("%d-%m-%Y"), Campaign.order_date.strftime("%d-%m-%Y")))

date_convert.short_description = 'Campaign'

class CampaignAdmin(admin.ModelAdmin):
    list_display = (date_convert, 'due_date', 'is_active')

admin.site.register(Campaign, CampaignAdmin)


