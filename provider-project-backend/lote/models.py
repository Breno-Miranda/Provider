from django.contrib.auth.models import User
from django.db import models
from campaign.models import Campaign
from company.models import Company


class Lote(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    sum_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_open = models.BooleanField(default=True, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.id)


