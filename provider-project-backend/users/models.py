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
    company = models.ForeignKey(Company, related_name="enterprise_bind", on_delete=None)
    user = models.ForeignKey(User,related_name="person_bind", on_delete=None)
    type = models.ForeignKey(Type, on_delete=None , null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=None , null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=None)
    is_business = models.BooleanField(default=False)
    is_individual = models.BooleanField(default=False)
    is_collaborator = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True

    def __str__(self):
        return self.user.username

#TODO: TERAR QUE RETIRAR FUTURAMENTE (FICARA ABSOLETO)
class Profile(models.Model):
    company = models.ForeignKey(Company, related_name="enterprise_profile", on_delete=None)
    user = models.ForeignKey(User, related_name="person_profile",  on_delete=None)
    cpf = models.BigIntegerField(default=False)
    rg = models.IntegerField()
    address = models.CharField(max_length=150)
    complement = models.CharField(max_length=150)
    reference = models.CharField(max_length=150, null=True, blank=True)
    neighborhood = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    number = models.CharField(max_length=20)
    birthday = models.DateField(null=True, blank=True)
    civil_sate = models.CharField(max_length=40, null=True, blank=True)
    date_register = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to='media/images')
    photo = models.ImageField(upload_to='media/images')
    about = models.CharField(max_length=150)
    is_term_accepted = models.BooleanField(default=False)
    
    class Meta:
        managed = True
        default_permissions = ('view' , 'add' ,  'delete' , 'change')
        
    def __str__(self):
        return self.user.first_name
        
class Collaborator(models.Model):
    company = models.ForeignKey(Company, related_name="enterprise_collaborator", on_delete=None ,  blank=True  ,  null=True)
    user_bond = models.ForeignKey(User, related_name="person_collaborator_bond",  on_delete=None ,  blank=True  ,  null=True)
    user = models.ForeignKey(User, related_name="person_collaborator", on_delete=None ,  blank=True  ,  null=True)
    registration = models.BigIntegerField(  blank=True  ,  null=True)
    code = models.BigIntegerField(  blank=True  ,  null=True)
    full_name = models.CharField(max_length=150   ,  blank=True  ,  null=True)
    cpf = models.BigIntegerField(  blank=True  ,  null=True)
    rg = models.IntegerField(  blank=True  ,  null=True)
    genre = models.CharField(max_length=2  ,  blank=True  ,  null=True)
    recommendation = models.BooleanField(default=False  ,  blank=True  ,  null=True)
    address = models.CharField(max_length=150  ,  blank=True  ,  null=True)
    complement = models.CharField(max_length=150  ,  blank=True  ,  null=True)
    reference = models.CharField(max_length=150  ,  blank=True  ,  null=True)
    neighborhood = models.CharField(max_length=150  ,  blank=True  ,  null=True)
    city = models.CharField(max_length=150   ,  blank=True  ,  null=True)
    state = models.CharField(max_length=2   ,  blank=True  ,  null=True)
    zipcode = models.IntegerField( blank=True  ,  null=True)
    number = models.CharField(max_length=20  ,  blank=True  ,  null=True)
    birthday = models.DateField(auto_now=True , blank=True  ,  null=True)
    civil_sate = models.CharField(max_length=40  ,  blank=True  ,  null=True)
    date_register = models.DateTimeField(auto_now_add=True ,  blank=True  ,  null=True)
    photo = models.ImageField(upload_to='photo/perfil'  , default="/anexo",  blank=True  ,  null=True)
    anexo = models.FileField(upload_to='anexo/doc/collaborator'  ,  default="/anexo", blank=True  ,  null=True)
    about = models.CharField(max_length=150  ,  blank=True  ,  null=True)
    is_term_accepted = models.BooleanField(default=False ,  blank=True  ,  null=True)
    is_active = models.BooleanField(default=False ,  blank=True  ,  null=True)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.user.first_name


class Individual(models.Model):
    company = models.ForeignKey(Company, related_name="enterprise_individual", on_delete=None)
    user_bond = models.ForeignKey(User, related_name="person_individual_bond",  on_delete=None ,  blank=True,  null=True)
    user = models.ForeignKey(User, related_name="person_individual",  on_delete=None ,  blank=True  ,  null=True)
    registration = models.BigIntegerField(null=True, blank=True)
    code = models.BigIntegerField(null=True, blank=True)
    cpf = models.BigIntegerField(null=True, blank=True)
    rg = models.IntegerField(null=True, blank=True)
    full_name = models.CharField(max_length=150   ,  blank=True  ,  null=True)
    genre = models.CharField(max_length=1)
    recommendation = models.BooleanField(default=False, null=True, blank=True)
    address = models.CharField(max_length=150)
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
    photo = models.ImageField(upload_to='photo/perfil')
    anexo = models.FileField(upload_to='anexo/doc/individual')
    about = models.CharField(max_length=150)
    is_term_accepted = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.user.first_name

class Busines(models.Model):
    company = models.ForeignKey(Company,related_name="enterprise_business", on_delete=None)
    user_bond = models.ForeignKey(User, related_name="person_business_bond",  on_delete=None ,  blank=True,  null=True)
    user = models.ForeignKey(User, related_name="person_business",  on_delete=None ,  blank=True,  null=True)
    registration = models.BigIntegerField(null=True, blank=True)
    code = models.BigIntegerField(null=True, blank=True)
    cnpj = models.BigIntegerField()
    recommendation = models.BooleanField(default=False, null=True, blank=True)
    company_name = models.CharField(max_length=150)
    social_name = models.CharField(max_length=150 , null=True, blank=True)
    fancy_name = models.CharField(max_length=150 , null=True, blank=True)
    state_registration = models.BigIntegerField(null=True, blank=True)
    municipal_registration = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=150)
    complement = models.CharField(max_length=150 , null=True, blank=True)
    reference = models.CharField(max_length=150, null=True, blank=True)
    neighborhood = models.CharField(max_length=150 ,  blank=True)
    city = models.CharField(max_length=150 , null=True, blank=True)
    state = models.CharField(max_length=2 , null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    date_register = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photo/perfil' ,  blank=True ,  null=True)
    anexo = models.FileField(upload_to='anexo/doc/business' ,  blank=True ,  null=True)
    about = models.CharField(max_length=150 ,  blank=True ,  null=True)
    is_term_accepted = models.BooleanField(default=False,  blank=True ,  null=True)
    is_active = models.BooleanField(default=False,  blank=True ,  null=True)

    class Meta:
        managed = True
        
    def __str__(self):
        return self.user.first_name

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