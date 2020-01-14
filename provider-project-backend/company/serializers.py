from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Company, Contact, Catalog

from common.serializers import CatalogSerializer


class CompanyContactSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields =  ('__all__') 
        
class CompanySerializer(serializers.ModelSerializer):
    
    _contact = CompanyContactSerializers(source='company', read_only=True)

    class Meta:
        model = Company
        fields = ("id", "name_company", "cnpj", "social_name", "fancy_name", "fancy_name", "address",
                  "complement", "reference", "email", "date_register", "logo" , "website" , "color_primary" , "color_secudary" , "_contact")

class CompanyKeySimplesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ("id", "name_company", "cnpj", "social_name", "fancy_name", "fancy_name", "address",
                  "complement", "reference", "email", "date_register" , "website", "logo")

class CompanyKeySecretSerializer(serializers.ModelSerializer):
    
    _contact = CompanyContactSerializers(source='Contact', read_only=True)

    class Meta:
        model = Company
        fields = ("id", "name_company", "cnpj", "social_name", "fancy_name", "fancy_name", "address",
                  "complement", "reference", "email", "date_register", "logo" , "website" , "_contact")


class CatalogCompanySerializer(ModelSerializer):
    
    _catalog = CatalogSerializer(source='catalog', read_only=True)

    class Meta:
        model = Catalog
        fields = ("company","reference","initial_date", "end_date","minimum_order", "_catalog")