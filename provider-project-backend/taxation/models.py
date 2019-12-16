from django.db import models
from company.models import Company

class Icm(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    description = models.CharField(max_length=150)
    icms_code_cfop = models.FloatField(max_length=200 , null=True, blank=True)
    icms_situation = models.IntegerField(null=True, blank=True)
    
    class Meta:
        managed = True

    def __str__(self):
        return self.description
    
class Ipi(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    description = models.CharField(max_length=150)
    ipi_framework = models.IntegerField(null=True, blank=True)
    ipi_situation = models.IntegerField(null=True, blank=True)
    ipi_aliquot = models.FloatField(max_length=200 , null=True, blank=True)
    
    class Meta:
        managed = True

    def __str__(self):
        return self.description

class Pis(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    description = models.CharField(max_length=150)
    situation = models.IntegerField(null=True, blank=True)
    aliquot = models.FloatField(max_length=200 , null=True, blank=True)
    
    class Meta:
        managed = True

    def __str__(self):
        return self.description
    
    
class Cofin(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    description = models.CharField(max_length=150)
    cofins_situation = models.IntegerField(null=True, blank=True)
    cofins_aliquot = models.FloatField(max_length=200 , null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.description
    
class Tax(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    description = models.CharField(max_length=150)
    tax_ref = models.CharField(max_length=150 , null=True, blank=True)
    is_active = models.BooleanField(default=False)
     
    class Meta:
        managed = True

    def __str__(self):
        return self.description


# class Tax(models.Model):
#     company = models.ForeignKey(Company, on_delete=None)
#     description = models.CharField(max_length=150)
#     tax_ref = models.CharField(max_length=150 , null=True, blank=True)
#     tax_icms = models.ForeignKey(Icm, related_name='icm', on_delete=None, null=True, blank=True)
#     tax_ipi = models.ForeignKey(Ipi, related_name='ipi', on_delete=None, null=True, blank=True)
#     tax_pis = models.ForeignKey(Pis, related_name='pis', on_delete=None , null=True, blank=True)
#     tax_cofins = models.ForeignKey(Cofin, related_name='cofin', on_delete=None , null=True, blank=True)
#     is_active = models.BooleanField(default=False)
     
#     class Meta:
#         managed = True

#     def __str__(self):
#         return self.description

