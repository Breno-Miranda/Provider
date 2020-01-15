from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

# Models
from django.contrib.auth.models import Permission, Group, User
from users.models import Contact, Bind, Profile, Type, Team, Sector, Bank_Account

# Serializers
from company.serializers import CompanySerializer


class TypeSerializers(ModelSerializer):
    class Meta:
        model = Type
        fields = ("__all__")


class TeamSerializers(ModelSerializer):
    class Meta:
        model = Team
        fields = ("__all__")


class SectorSerializers(ModelSerializer):
    class Meta:
        model = Sector
        fields = ("__all__")


class ProfileSerializers(ModelSerializer):
    class Meta:
        model = Profile
        fields = ("__all__")


class UsersAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'groups', 'user_permissions')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("__all__")


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("__all__")


class UserBindSerializers(serializers.ModelSerializer):

    _company = CompanySerializer(source='company', read_only=True)
    _type = TypeSerializers(source='type', read_only=True)
    _team = TeamSerializers(source='team', read_only=True)
    _sector = SectorSerializers(source='sector', read_only=True)
    _user = UsersSerializer(source='user', read_only=True)

    class Meta:
        model = Bind
        fields = ('id', 'user', 'is_active', '_company', '_type', '_team',
                  '_sector', '_user')


# INFORMATION USER CATEGORY FIXED SYSTEM
class ContactsSerializers(ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", "phone", "email", "cell")


class BankAccountUsersSerializers(ModelSerializer):
    class Meta:
        model = Bank_Account
        fields = ("id", "account", "agency", "bank", "type_account",
                  "kind_of_person")


class UserBindProfileSerializers(ModelSerializer):

    _bind = UserBindSerializers(source='bind', read_only=True)

    class Meta:
        model = Profile
        fields = ("id", "matriculation", "full_name", "company", "user_bind",
                  "bind", "cpf", "rg", "genre", "recommendation", "address",
                  "complement", "reference", "neighborhood", "city", "state",
                  "zipcode", "number", "birthday", "civil_sate",
                  "date_register", "photo", "anexo", "about",
                  "is_term_accepted", "is_active", "_bind")
