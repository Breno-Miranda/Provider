from django.contrib.auth.models import User
from django.db import models
from company.models import Company

class Type(models.Model):
    type = models.CharField(max_length=150)
    code = models.IntegerField()
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True

    def __str__(self):
        return self.type

class Team(models.Model):
    company = models.ForeignKey(Company,related_name="enterprise_team", on_delete=None)
    name = models.CharField(max_length=150)
    descripiton = models.CharField(max_length=150, null=True, blank=True)
    number = models.IntegerField()
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True

    def __str__(self):
        return self.name
    
class Sector(models.Model):
    company = models.ForeignKey(Company, related_name="enterprise_sector", on_delete=None)
    name = models.CharField(max_length=150)
    descripiton = models.CharField(max_length=150, null=True, blank=True)
    number = models.IntegerField()
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True

    def __str__(self):
        return self.name
    
    
class Bind(models.Model):
    company = models.ForeignKey(Company, related_name="comapny_bind", on_delete=None)
    user = models.ForeignKey(User, related_name="user_bind", on_delete=None)
    type = models.ForeignKey(Type, on_delete=None , null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=None , null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=None, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True

    def __str__(self):
        return self.user.username
    

class Profile(models.Model):
    matriculation = models.BigIntegerField(null=True, blank=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=None)
    user = models.ForeignKey(User,  on_delete=None ,  blank=True,  null=True)
    user_link = models.ForeignKey(User, related_name="user_link",  on_delete=None ,  blank=True,  null=True)
    bind = models.ForeignKey(Bind, related_name="bind_user",  on_delete=None ,  blank=True,  null=True)
    cpf = models.BigIntegerField(null=True, blank=True)
    rg = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=1, default='F')
    recommendation = models.BooleanField(default=False, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    complement = models.CharField(max_length=150 , null=True, blank=True)
    reference = models.CharField(max_length=150, null=True, blank=True)
    neighborhood = models.CharField(max_length=150 , null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True )
    state = models.CharField(max_length=2 , null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    civil_sate = models.CharField(max_length=40, null=True, blank=True)
    date_register = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photo/perfil', null=True, blank=True)
    anexo = models.FileField(upload_to='anexo/doc/individual', null=True, blank=True)
    about = models.CharField(max_length=150, null=True, blank=True)
    is_term_accepted = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.full_name


class Contact(models.Model):
    company = models.ForeignKey(Company,related_name="enterprise_contact", on_delete=None)
    user = models.ForeignKey(User, related_name="person_contact",  on_delete=None)
    phone = models.BigIntegerField( null=True, blank=True)
    cell = models.BigIntegerField( null=True, blank=True)
    email = models.CharField(max_length=150 , null=True, blank=True)
    main = models.BooleanField(default=False,  blank=True ,  null=True)
    is_active = models.BooleanField(default=False,  blank=True ,  null=True)
     
    class Meta:
        managed = True
        
    def __str__(self):
        return self.user.first_name
    
class Bank_Account(models.Model):
    company = models.ForeignKey(Company,related_name="enterprise_bankAccount", on_delete=None)
    user = models.ForeignKey(User, related_name="person_bankAccount",  on_delete=None)
    account = models.IntegerField(null=True, default=0,blank=True)
    agency = models.IntegerField(null=True, default=0,blank=True)
    bank = models.CharField(max_length=150 , null=True, blank=True)
    type_account = models.CharField(max_length=2 , null=True, blank=True)
    kind_of_person =  models.CharField(max_length=2 , null=True, blank=True)
    main = models.BooleanField(default=False,  blank=True ,  null=True)
    is_active = models.BooleanField(default=False,  blank=True ,  null=True)
    

    class Meta:
        managed = True
        
    def __str__(self):
        return self.user.first_name

    
class Level(models.Model):
    company = models.ForeignKey(Company,related_name="enterprise_level", on_delete=None)
    user = models.ForeignKey(User, related_name="person_level",  on_delete=None)
    type = models.ForeignKey(Type, on_delete=None)
    nivel = models.CharField(max_length=150)
    discount = models.FloatField(max_length=200)
    minimum_order = models.IntegerField()
    value = models.FloatField(max_length=200)
    amount_of_points = models.IntegerField() 
    value_of_points = models.FloatField(max_length=200)
    start_point_range = models.IntegerField() 
    end_point_range = models.IntegerField()
    term_payment = models.IntegerField()
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.nivel
    
class Goal(models.Model):
    company = models.ForeignKey(Company,related_name="enterprise_goal", on_delete=None)
    user = models.ForeignKey(User, related_name="person_goal",  on_delete=None)
    type = models.ForeignKey(Type, on_delete=None)
    goal = models.CharField(max_length=150)
    discount = models.FloatField(max_length=200)
    minimum_order = models.IntegerField()
    value = models.FloatField(max_length=200)
    amount_of_points = models.IntegerField() 
    value_of_points = models.FloatField(max_length=200)
    start_point_range = models.IntegerField() 
    end_point_range = models.IntegerField()
    term_payment = models.IntegerField()
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.goal
