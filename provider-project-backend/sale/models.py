from django.db import models
from request.models import Request
from company.models import Company
from django.contrib.auth.models import User
from users.models import  Individual, Busines

from django.utils import timezone

class Status(models.Model):
    company = models.ForeignKey(Company, related_name="status_sale" , on_delete=None)
    type = models.CharField(max_length=150)
    initials = models.CharField(max_length=1 ,  blank=True  ,  null=True)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.type

    
class Flags_card(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    number = models.IntegerField() 
    type = models.CharField(max_length=150)
    initials = models.CharField(max_length=1 ,  blank=True  ,  null=True)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.type
    
class Payment_form(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    number = models.IntegerField() 
    type = models.CharField(max_length=150) 
    initials = models.CharField(max_length=1 ,  blank=True  ,  null=True)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True
    
    def __str__(self):
        return self.type
    
class Accrediting(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    name = models.CharField(max_length=150)
    cnpj = models.BigIntegerField()
    number_code = models.CharField(max_length=50 ,  blank=True  ,  null=True)
    initials = models.CharField(max_length=1 ,  blank=True  ,  null=True)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True
    
    def __str__(self):
        return self.name

class Nature_operation(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        managed = True
    
    def __str__(self):
        return self.name
    
class Sale(models.Model):
    company = models.ForeignKey(Company, on_delete=None)
    user = models.ForeignKey(User, on_delete=None)
    request = models.ForeignKey(Request, on_delete=None ,  blank=True  ,  null=True)
    individual = models.ForeignKey(Individual, on_delete=None ,  blank=True  ,  null=True)
    business = models.ForeignKey(Busines, on_delete=None ,  blank=True  ,  null=True)
    status = models.ForeignKey(Status, on_delete=None, default=1,  null=True, blank=True)
    nature_operation = models.ForeignKey(Nature_operation, on_delete=None ,  blank=True  ,  null=True) # natureza_operacao
  
    NORMAL = 1 
    DEVOLUTION_RETURN = 4 

    FINALITY_TYPE = [
        (NORMAL, 'NF-e normal'),
        (DEVOLUTION_RETURN, 'Devolução/Retorno'),
    ]
    
    finality = models.IntegerField(choices=FINALITY_TYPE, default=NORMAL) # FINALIDADE 
    
    EXIT = 1 
    INPUT = 0 

    OPERATION_TYPE = [
        (EXIT, 'Saída'),
        (INPUT, 'Entrada'),
    ]
    
    operation = models.IntegerField(choices=OPERATION_TYPE, default=EXIT) # OPERAÇÃO 
    
    NFE = 1 
    NFCE = 2
    
    MODEL_TYPE = [
        (NFE, 'NF-e'),
        (NFCE, 'NFC-e'),
    ]
    
    template = models.IntegerField(choices=MODEL_TYPE, default=NFCE) # OPERAÇÃO 
    
    PRO = 1 
    HOM = 2
    
    AMBIENTE_TYPE = [
        (PRO, '1 - Produção'),
        (HOM, '2 - Homologação'),
    ]
    
    ambiente = models.IntegerField(choices=AMBIENTE_TYPE, default=HOM) # AMBIENTE 
    
    TEF = 1 
    POS = 2 

    INTEGRATION_TYPE = [
        (TEF, '1 - Pagamento integrado com o sistema de automação da empresa (Ex: equipamento TEF, Comércio eletrônico)'),
        (POS, '2 - Pagamento não integrado com o sistema de automação da empresa (Ex: equipamento POS)'),
    ]
    
    flags_card = models.ForeignKey(Flags_card, on_delete=None ,  blank=True  ,  null=True)
    payment_form = models.ForeignKey(Payment_form, on_delete=None ,  blank=True  ,  null=True)
    payment_form_amount = models.IntegerField(null=True, blank=True)
    accrediting = models.ForeignKey(Accrediting, on_delete=None ,  blank=True  ,  null=True)
    integration_type = models.IntegerField(choices=INTEGRATION_TYPE, default=POS)
    nsu_authorization = models.BigIntegerField(default=False,  blank=True  ,  null=True)
    date_create = models.DateTimeField(default=timezone.now)
    
    NOT = 0 
    OPL = 1 
    ONPI = 2 
    ONPT = 3 
    NOED = 4  
    OPFE = 5 
    ONPO = 9 

    PRESENCE_TYPE = [
        (NOT, '0 - Não se aplica (por exemplo, Nota Fiscal complementar ou de ajuste)'),
        (OPL, '1 - Operação presencial'),
        (ONPI, '2 - Operação não presencial, pela Internet'),
        (ONPT, '3 - Operação não presencial, Teleatendimento'),
        (NOED, '4 - NFC-e em operação com entrega a domicílio'),
        (OPFE, '5 - Operação presencial, fora do estabelecimento'),
        (ONPO, '9 - Operação não presencial, outros'),
    ]

    presence = models.IntegerField(choices=PRESENCE_TYPE, default=OPL)  #PRESENÇA
    
    CIF = 0 
    FOB = 1 
    CFD = 2 
    CFR = 3 
    TPD = 4  
    SOT = 9 

    FREE_MODEL_TYPE = [
        (CIF, '0 - Contratação do Frete por conta do Remetente (CIF)'),
        (POS, '1 - Contratação do Frete por conta do Destinatário (FOB)'),
        (FOB, '2 - Contratação do Frete por conta de Terceiros'),
        (CFD, '3 - Transporte Próprio por conta do Remetente'),
        (TPD, '4 - Transporte Próprio por conta do Destinatário'),
        (SOT, '9 - Sem Ocorrência de Transporte'),
    ]

    free_model = models.IntegerField(choices=FREE_MODEL_TYPE, default=CFR) # MODALIDADE DE FRETE
    
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    freight = models.DecimalField(max_digits=10, decimal_places=2)
    change = models.DecimalField(max_digits=10, decimal_places=2,  blank=True  ,  null=True)
    date_register = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = True
        
    def __str__(self):
        return self.user.username