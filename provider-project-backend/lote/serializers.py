from rest_framework.serializers import ModelSerializer
from .models import Lote

class LotsSerializers(ModelSerializer):
    
    class Meta:
        model = Lote
        fields = ("__all__")
