from django.db import models
# Create your models here.
from lote.models import Lote
from product.models import Product
from company.models import Company, Catalog
from django.contrib.auth.models import User
from users.models import Individual, Busines, Bind
from common.models import Payment_methods

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
    lot = models.ForeignKey(Lote, on_delete=None)
    catalog = models.ForeignKey(Catalog, on_delete=None)
    user = models.ForeignKey(User, on_delete=None)
    user_bind = models.ForeignKey(Bind, on_delete=None, blank=True, null=True)
    is_user_bind = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=None, blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    billing_date = models.DateTimeField(null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    payment_methods = models.ForeignKey(Payment_methods, on_delete=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount_commission = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    commission_customer = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    freight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    request_number = models.BigIntegerField(null=True, blank=True)
    observation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.amount)
    
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
