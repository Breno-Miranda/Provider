from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Product , Category ,Color , Gallery , Status

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    
    # Relation field forenkey
    _category =  CategorySerializer(source='category', read_only=True)
    
    # Modificando field
    bind_name = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('product', 'ean', 'description', 'unidade', 'ncm', 'sale_price', 'bind_name', 'amount', 'discount', '_category')
        
    
    def get_product(self, obj):
        return obj.id
    
    def get_discount(self, obj):
        return 0.0
    
    def get_amount(self, obj):
        return 1
    
    def get_bind_name(self, obj):
        return '{}   {} '.format(obj.ean ,obj.description) 
    
    
class StatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Status
        fields = ('__all__')

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('__all__')

class ProductNewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ( 'ean' , 'description' , 'unidade' , 'ncm' , 'origin', 'cest' , 'sale_price' , 'resale_price','discount' ,
                   'amount' , 'category' , 'company', 'status' , 'taxation' )
  