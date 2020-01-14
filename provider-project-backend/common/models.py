from django.db import models


class Provider(models.Model):
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
    provider = models.ForeignKey(Provider, on_delete=None)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=150)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.company.company_name


class Zone(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
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


class Payment_methods(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=150)
    initials = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)

    class Meta:
        managed = True

    def __str__(self):
        return self.type


class Flags_card(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=150)
    initials = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)

    class Meta:
        managed = True

    def __str__(self):
        return self.type
