from rest_framework.serializers import ModelSerializer
from .models import Provider, Catalog

class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = ("__all__")
        
class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = ("__all__")