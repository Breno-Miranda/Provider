from django.db import models
from company.models import Company

# Create your models here.
class Provider(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    cnpj = models.BigIntegerField()
    company_name = models.CharField(max_length=150)
    social_name = models.CharField(max_length=150)
    fancy_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    complement = models.CharField(max_length=150)
    reference = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    number = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    date_register = models.DateTimeField(auto_now_add=True)
    is_term_accepted = models.BooleanField(default=False)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.company_name
    
class Contacts(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    provider = models.ForeignKey(Provider, on_delete=None)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=150)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.company.company_name


