from rest_framework.serializers import ModelSerializer
from models import Provider

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ("_all_")