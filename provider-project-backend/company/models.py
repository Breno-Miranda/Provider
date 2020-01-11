import os
import binascii
import jwt
import json

from django.db import models
from django.core import serializers
from time import time # para geracao da timestamp
from common.models import Catalog

class Plan(models.Model):
    description = models.CharField(max_length=200)
    discount = models.FloatField(max_length=200)
    number_plan = models.IntegerField()
    token = models.CharField(max_length=200)
    amount_of_points = models.IntegerField() 
    value_of_points = models.FloatField(max_length=200)
    resale_price = models.DecimalField(max_digits=10, decimal_places=2 , null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2 , null=True, blank=True)
    term_payment = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.description

class Company(models.Model):
    plan = models.ForeignKey(Plan, related_name="plan_company" , on_delete=None)
    cnpj = models.BigIntegerField()
    name_company = models.CharField(max_length=150)
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
    color_primary = models.CharField(max_length=150)
    color_secudary = models.CharField(max_length=150)
    website = models.CharField(max_length=250)
    date_register = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_term_accepted = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='images/company')
       
    
    class Meta:
        managed = True 

    def __str__(self):
        return self.name_company
    
class Contact(models.Model):
    company = models.ForeignKey(Company, related_name="contact_company" , on_delete=None)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=150)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.company.name_company




class Key(models.Model):
    company = models.OneToOneField(Company, related_name="key_company" , on_delete=None)
    simples_key = models.CharField(max_length=255, default='Simples key', null=True, blank=True)
    secret_key = models.CharField(max_length=255, default='Secret key',null=True, blank=True)
 
    def save(self, *args, **kwargs):
        
        obj = Company.objects.get(id=self.company.id)
      
        payload_simples = {
            'id': obj.id,
            'is_all': False,
        }
       
        payload_secret = {
            'id': obj.id,
            'is_all': True,
        }

        self.simples_key = jwt.encode(payload_simples, 'ZTkXVpBwEkW4S32roccJKg==', algorithm='HS256').decode('utf-8')

        self.secret_key = jwt.encode(payload_secret, '7bh1bROfZEKtOzqD5n5t8w==', algorithm='HS256').decode('utf-8')

        super(Key, self).save(*args, **kwargs)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.company.name_company


class Catalog(models.Model):
    reference = models.BigIntegerField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, null=True, blank=True)
    initial_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    minimum_order = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.reference
