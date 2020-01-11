from django.db import models
from company.models import Company
from taxation.models import Tax
from users.models import Bind, Type

class Status(models.Model):
    company = models.ForeignKey(Company, related_name="status_product",  on_delete=None)
    type = models.CharField(max_length=150)
    initials = models.CharField(max_length=1, null=True, blank=True)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
      
    class Meta:
        managed = True
    
    def __str__(self):
        return self.type
    
class Color(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    type = models.CharField(max_length=150)
    initials = models.CharField(max_length=1, null=True, blank=True)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
      
    class Meta:
        managed = True
    
    def __str__(self):
        return self.type
    
class Category(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    type = models.CharField(max_length=150)
    initials = models.CharField(max_length=1, null=True, blank=True)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    discount = models.FloatField(max_length=200)
    
    class Meta:
        managed = True
    
    def __str__(self):
        return self.type
  
class Product(models.Model):
    reference = models.BigIntegerField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=None , blank=True)
    status = models.ForeignKey(Status, on_delete=None , blank=True)
    category = models.ForeignKey(Category, on_delete=None , blank=True)
    description = models.CharField(max_length=250 , null=True, blank=True)
    ean = models.BigIntegerField(default=False, null=True, blank=True)
    ncm = models.FloatField(default=False, null=True, blank=True)
    unidade = models.CharField(max_length=150 , null=True, blank=True)
    cest = models.BigIntegerField(default=False, null=True, blank=True) 
    amount = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    origin = models.IntegerField(null=True, blank=True)
    discount = models.FloatField(max_length=200 , null=True, blank=True)
    resale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2) 
    taxation = models.ForeignKey(Tax, on_delete=None , blank=True)
    page = models.BigIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    value_provider = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    type_value_provider = models.CharField(null=True, blank=True)
    stock = models.BigIntegerField(default=0)
    size = models.CharField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    last_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(Bind, on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)

    
    class Meta:
        managed = True

    def __str__(self):
        return self.description

class Gallery(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    product = models.ForeignKey(Product, on_delete=None)
    photo = models.ImageField(upload_to='products')
    url_thubnail = models.CharField(max_length=150 , null=True, blank=True)
    initials = models.CharField(max_length=1 , null=True, blank=True)
    description = models.CharField(max_length=150 , null=True, blank=True)
    is_active = models.BooleanField(default=False , null=True, blank=True)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.photo
