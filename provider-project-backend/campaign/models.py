from django.db import models
from django.contrib.auth.models import User
from company.models import Company

class Campaign (models.Model):
    company = models.ForeignKey(Company,  on_delete=None)
    order_date = models.DateTimeField(null=True, blank=True)
    send_date = models.DateTimeField(null=True, blank=True)
    arrival_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.order_date.strftime("%Y-%m-%d"))


