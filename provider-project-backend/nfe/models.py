from django.db import models

from company.models import Company

class Setting(models.Model):
    company = models.ForeignKey(Company, related_name="enterprise", on_delete=None)
    consumer_key = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    consumer_secret = models.CharField(max_length=255)
    access_token_secret = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True

    def __str__(self):
        return self.company.name_company