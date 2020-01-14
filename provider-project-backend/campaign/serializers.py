from rest_framework.serializers import ModelSerializer
from .models import Campaign

class CampaignSerializers(ModelSerializer):
    
    class Meta:
        model = Campaign
        fields = ("__all__")
