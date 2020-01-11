from django.db import models
from provider.models import Provider

class Zone(models.Model):
    name = models.CharField(null=True, blank=True)
    initials = models.CharField(max_length=4, null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name


class Catalog(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    commission = models.FloatField(blank=True, null=True)
    initials = models.CharField(max_length=3)
    cover = models.ImageField(upload_to='catalog', null=True, blank=True)
    pdf = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(null=True, blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.name
