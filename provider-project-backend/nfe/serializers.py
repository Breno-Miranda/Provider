from rest_framework.serializers import ModelSerializer
from company.models import Company

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "name_company", "cnpj", "social_name", "fancy_name", "fancy_name", "address",
                  "complement", "reference", "email", "date_register", "is_term_accepted")
