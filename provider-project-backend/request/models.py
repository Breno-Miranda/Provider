from django.db import models
# Create your models here.
from product.models import Product
from company.models import Company
from django.contrib.auth.models import User
from users.models import  Individual, Busines


class Status(models.Model):
    company = models.ForeignKey(Company, related_name="enterprise_request_status", on_delete=None)
    type = models.CharField(max_length=150)
    initials = models.CharField(max_length=1 , null=True, blank=True)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.type

class Request(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    user = models.ForeignKey(User, on_delete=None)
    individual = models.ForeignKey(Individual, on_delete=None ,  blank=True  ,  null=True)
    business = models.ForeignKey(Busines, on_delete=None ,  blank=True  ,  null=True)
    status = models.ForeignKey(Status, on_delete=None,  blank=True  ,  null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2 , null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    freight = models.DecimalField(max_digits=10, decimal_places=2 ,  null=True, blank=True)
    amount =  models.IntegerField(null=True)
    observation = models.CharField(max_length=255, null=True, blank=True)
    date_register = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
    
class Itens(models.Model):
    request = models.ForeignKey(Request, on_delete=None)
    product = models.ForeignKey(Product, on_delete=None)
    amount = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2 ,  blank=True  ,  null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    is_checked = models.BooleanField(blank=True,null=True)
     
    def __str__(self):
        return self.request.user.first_name