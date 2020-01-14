from rest_framework.serializers import ModelSerializer

from .models import Status, Request, Itens

from product.serializers import ProductSerializer
from product.models import Product

from users.serializers import UsersSerializer
from company.serializers import CatalogCompanySerializer


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
    
    _user = UsersSerializer(source='user', read_only=True)
    _status = StatusSerializers(source='status', read_only=True)
    _catalog = CatalogCompanySerializer(source='catalog', read_only=True)
    
    class Meta:
        model = Request
        fields = ("id", "company", "lot", "is_user_bind", "create_date",  "billing_date",  "payment_date",  "return_date", "payment_methods", "amount", "amount_paid",  "amount_commission",  "commission_customer",  "freight",  "discount",  "request_number", "observation", "_user" , "_status", "_catalog")
