from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Status, Request, Itens

from product.serializers import ProductSerializer
from product.models import Product

from users.serializers import UsersSerializer, ProfileSerializers
from company.serializers import CatalogCompanySerializer
from campaign.serializers import CampaignSerializers
from users.serializers import UserBindProfileSerializers

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
    
    _profile = ProfileSerializers(source='profile', read_only=True)
    _status = StatusSerializers(source='status', read_only=True)
    _catalog = CatalogCompanySerializer(source='catalog', read_only=True)
    _campaign = CampaignSerializers(source='campaign', read_only=True)

    create_date = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Request
        fields = ("id", "company", "lot",  "profile", "user_bind_typeit", "create_date",  "billing_date",  "payment_date",
                  "return_date", "payment_methods", "amount", "amount_paid",  "amount_commission",  "commission_customer",
                  "freight",  "discount",  "request_number", "observation", "_profile" , "_status", "_catalog" , "_campaign")

    def get_create_date(self, obj):
        return str(obj.create_date.strftime("%d-%m-%Y"))


# serializer to insert

class requestCreateSerializers(ModelSerializer):
    
    class Meta:
        model = Request
        fields = ("company", "campaign",  "lot", "catalog", "profile", "amount", "user_bind_typeit")
        
class requestItensCreateSerializers(ModelSerializer):
    
    class Meta:
        model = Itens
        fields = ("request" , "product" , "amount" , "total")
