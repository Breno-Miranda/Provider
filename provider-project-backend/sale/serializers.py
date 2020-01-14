from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from common.models import Payment_methods
from .models import  Flags_card, Accrediting, Nature_operation, Sale


class PaymentFormSerializers(serializers.ModelSerializer):

	class Meta:
	    model = Payment_methods
	    fields = ("__all__")

class FlagsCardSerializers(serializers.ModelSerializer):

	class Meta:
	    model = Flags_card
	    fields = ("__all__")

class AccreditingSerializers(serializers.ModelSerializer):

	class Meta: 
	    model = Accrediting
	    fields = ("__all__")

class NatureOperationSerializers(serializers.ModelSerializer):

	class Meta:
	    model = Nature_operation
	    fields = ("__all__")

class SaleSerializers(serializers.ModelSerializer):
    
    
	# date_register = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d", 'iso-8601'])
    
	class Meta: 
		model = Sale
		fields = ("__all__")
  
