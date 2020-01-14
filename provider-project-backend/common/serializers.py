from rest_framework.serializers import ModelSerializer
from .models import Provider, Catalog

class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = ("_all_")
        
class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = ("_all_")