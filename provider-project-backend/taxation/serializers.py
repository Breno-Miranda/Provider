from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Tax, Cofin, Icm ,Ipi ,Pis
        
class TaxCofinsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cofin
        fields = ('__all__')
        
class TaxIcmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Icm
        fields = ('__all__')
        
class TaxIpiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ipi
        fields = ('__all__')
    
class TaxPisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pis
        fields = ('__all__')

class TaxSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tax
        fields = ('__all__')
  