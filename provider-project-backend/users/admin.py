from django.contrib import admin
from .models import Bind, Type, Team, Sector , Contact, Profile, Bank_Account

admin.site.empty_value_display = '(empty)'


class BindAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'type', 'team', 'sector', 'user_link', 'is_active')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('bind', 'user', 'full_name', 'company', 'cpf')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'code', 'is_active')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'descripiton', 'number', 'is_active')

class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'descripiton', 'number', 'is_active')



admin.site.register(Bind, BindAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Contact) 
admin.site.register(Bank_Account) 
admin.site.register(Profile, ProfileAdmin)

