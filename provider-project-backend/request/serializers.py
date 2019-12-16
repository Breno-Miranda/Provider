from rest_framework.serializers import ModelSerializer

from .models import Status, Request, Itens

from product.serializers import ProductSerializer
from product.models import Product

class StatusSerializers(ModelSerializer):
    
    class Meta:
        model = Status
        fields = ("__all__")
        
class ItensSerializers(ModelSerializer):
    
    _product = ProductSerializer(source='product', read_only=True)
    
    class Meta:
        model = Itens
        fields = ("id", "amount", "discount", "subtotal" , "total", "is_checked", "request" , "product" ,  "_product")
        
class RequestSerializers(ModelSerializer):
    
    class Meta:
        model = Request
        fields = ("__all__" )
