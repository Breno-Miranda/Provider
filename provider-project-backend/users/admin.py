from django.contrib import admin
from .models import Bind, Type, Team, Sector , Contact, Busines, Individual, Profile, Collaborator, Bank_Account


admin.site.register(Bind)
admin.site.register(Type)
admin.site.register(Team)
admin.site.register(Sector)
admin.site.register(Contact) 
admin.site.register(Bank_Account) 
admin.site.register(Profile)

admin.site.register(Busines)
admin.site.register(Individual) 
admin.site.register(Collaborator) 