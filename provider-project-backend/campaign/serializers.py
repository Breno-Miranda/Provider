from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Campaign


class CampaignSerializers(ModelSerializer):

    order_date = serializers.DateTimeField(format="%d-%m-%Y")
    send_date = serializers.DateTimeField(format="%d-%m-%Y")
    order_send_name = serializers.SerializerMethodField()

    class Meta:
        model = Campaign
        fields = ("id", "company", "order_date", "send_date", "arrival_date",
                  "due_date", "return_date", "user", "is_active",
                  "create_date" , "order_send_name")

    def get_order_send_name(self, obj):
        return str(obj.order_date.strftime("%d-%m-%Y")) +' à '+ str(obj.send_date.strftime("%d-%m-%Y"))