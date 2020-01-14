from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import Permission, Group, User
from users.models import Contact, Bank_Account, Profile, Bind
from .serializers import ContactsSerializers, GroupSerializer, PermissionSerializer, UsersSerializer, \
    UserBindSerializers, BankAccountUsersSerializers, ProfileSerializers, UserBindProfileSerializers

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN,
                                   HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND,
                                   HTTP_200_OK)

from django.db.models import Q
from core import pagination
from rest_framework import permissions
from rest_framework.decorators import action
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_admin


class ProfileViewSet(viewsets.ViewSet):
    def list(self, request):

        if not request.user.has_perm('users.view_profile'):
            return Response(
                {
                    'msm':
                    'Sem permissão de visualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        companyId = request.GET.get('company_id', None)
        type_user_number = request.GET.get('type_user_number', None)

        try:

            if not type_user_number:
                queryset_profile = UserBindProfileSerializers(
                    Profile.objects.all().filter(company_id=companyId), many=True)

            else:

                queryset_profile = UserBindProfileSerializers(
                    Profile.objects.all().filter(company_id=companyId,
                                                bind__type__code=type_user_number),
                    many=True)

            return Response(queryset_profile.data, status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! Houve um erro na listagem dos dados.  Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def create(self, request):

        if not request.user.has_perm('users.create_profile'):
            return Response(
                {
                    'msm':
                    'Sem permissão de criação. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        try:
            serializerProfile = ProfileSerializers(data=request.data)
            if serializerProfile.is_valid():
                serializerProfile.save()
                return Response(
                    {
                        'success': 'Heey! Ação efetuado acom sucesso.',
                        'status': True
                    },
                    status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! Houve um erro na inserção dos dados.  Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):

        if not request.user.has_perm('users.update_profile'):
            return Response(
                {
                    'msm':
                    'Sem permissão de atualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        try:
            profile = ProfileSerializers(
                Profile.objects.get(id=pk, company_id=companyId))
            serializerProfile = ProfileSerializers(profile, data=request.data)
            if serializerProfile.is_valid():
                serializerProfile.save()
                return Response(
                    {
                        'success': 'Heey! Ação efetuado acom sucesso.',
                        'status': True
                    },
                    status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! Houve um erro na atualização dos dados.  Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):

        if not request.user.has_perm('provider.delete_profile'):
            return Response(
                {
                    'msm':
                    'Sem permissão de exclusão. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)
        try:
            individual = ProfileSerializers(
                Profile.objects.get(id=pk, company_id=companyId))
            individual.is_active = request.data['is_active']
            individual.save()
            return Response(
                {
                    'success': 'Heey! Ação efetuado acom sucesso.',
                    'status': True
                },
                status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! Houve um erro na exclusão dos dados.  Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]


# Auth Permission

# modulo criado para liberação de permissões ao usuario.
# precisa adicionar os GRUPOS para facilitar para o usuario MASTER


class PermissionViewSet(viewsets.ViewSet):
    def list(self, request):

        companyId = request.GET.get('company_id', None)

        if not request.user.has_perm('auth.view_permission'):
            return Response(
                {
                    'msm':
                    'Sem permissão de visualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': False
                },
                status=HTTP_403_FORBIDDEN)

        try:
            querysetPermission = PermissionSerializer(Permission.objects.all(),
                                                      many=True)

            querysetUsers = UserBindSerializers(
                Bind.objects.all().filter(company_id=companyId),
                many=True,
                context={"request": request})

            queryGroup = GroupSerializer(Group.objects.all(), many=True)

            queryset = {
                "permission": querysetPermission.data,
                "users": querysetUsers.data,
                'groups': queryGroup.data
            }
            return Response(queryset, status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    'ops, aconteceu algum problema com as permissões. Tente novamente.',
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def create(self, request):

        if not request.user.has_perm('auth.add_permission'):
            return Response(
                {
                    'msm':
                    'Sem permissão de criação. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True,
                },
                status=HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=request.data['user_id'])
            if request.data['group_id']:
                groups = Group.objects.get(pk=request.data['group_id'])
                user.groups.add(groups)
            if request.data['permission_id']:
                permission = Permission.objects.get(
                    pk=request.data['permission_id'])
                user.user_permissions.add(permission)

            return Response(
                {
                    'success': 'Alteração efetuada com sucesso.',
                    'status': True
                },
                status=HTTP_200_OK)
        except:
            return Response(
                {
                    'error':
                    'Error ao alterar as permissões, certifique-se se tudo ocorreu como o correto e tente novamente.',
                    'status': False
                },
                status=HTTP_404_NOT_FOUND)

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]


class UsersViewSet(viewsets.ViewSet):
    def list(self, request):

        companyId = request.GET.get('company_id', None)

        if not request.user.has_perm('users.view_bind'):
            return Response(
                {
                    'msm':
                    'Sem permissão de visualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        try:
            queryset = UserBindSerializers(
                Bind.objects.all().filter(company_id=companyId),
                many=True,
                context={"request": request})
            return Response(queryset.data, status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm': '0 usuarios cadastrados.',
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]


# USER ACCOUNTVIEW ENDPOINT
class UserAccountViewSet(viewsets.ViewSet):
    def list(self, request):

        if not request.user.has_perm('users.view_bank_account'):
            return Response(
                {
                    'msm':
                    'Sem permissão de visualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        companyId = request.GET.get('company_id', None)
        user_id = request.GET.get('user_id', None)

        try:
            queryset_bankaccount = BankAccountUsersSerializers(
                Bank_Account.objects.filter(company_id=companyId,
                                            user_id=user_id,
                                            main=1,
                                            is_active=1).first())
            return Response(queryset_bankaccount.data, status=HTTP_200_OK)
        except:
            return Response({
                'msm': 'Sem informações.',
                'status': 'danger'
            },
                            status=HTTP_404_NOT_FOUND)

    def create(self, request):

        if not request.user.has_perm('users.view_add'):
            return Response(
                {
                    'msm':
                    'Sem permissão de criação. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_400_BAD_REQUEST)

        try:
            serializerBankAccount = BankAccountUsersSerializers(
                data=request.data)
            if serializerBankAccount.is_valid():
                serializerBankAccount.save()
                return Response(
                    {
                        'success': 'Heey! Ação efetuado acom sucesso.',
                        'status': True
                    },
                    status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! Houve um erro na atualização dos dados. Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):

        if not request.user.has_perm('users._bind'):
            return Response(
                {
                    'msm':
                    'Sem permissão de atualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        try:
            bankaccount = Bank_Account.objects.get(
                id=request.data["bankaccount_id"],
                company_id=request.data["company_id"],
                user_id=request.data["user_id"],
                main=1,
                is_active=1)
            serializerBankAccount = BankAccountUsersSerializers(
                bankaccount, data=request.data)
            if serializerBankAccount.is_valid():
                serializerBankAccount.save()
                return Response(
                    {
                        'success': 'Heey! Ação efetuado acom sucesso.',
                        'status': True
                    },
                    status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! Houve um erro na atualização dos dados.  Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]


# USER CONTACTVIEW ENDPOINT
class UserContactViewSet(viewsets.ViewSet):
    def list(self, request):

        if not request.user.has_perm('users.view_contact'):
            return Response(
                {
                    'msm':
                    'Sem permissão de visualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        companyId = request.GET.get('company_id', None)
        user_id = request.GET.get('user_id', None)

        try:
            queryset_contact = ContactsSerializers(
                Contact.objects.filter(company_id=companyId,
                                       user_id=user_id,
                                       main=1,
                                       is_active=1).first())
            return Response(queryset_contact.data, status=HTTP_200_OK)
        except:
            return Response({
                'msm': 'Sem informações.',
                'status': 'danger'
            },
                            status=HTTP_404_NOT_FOUND)

    def create(self, request):

        if not request.user.has_perm('users.create_contact'):
            return Response(
                {
                    'msm':
                    'Sem permissão de criação. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_400_BAD_REQUEST)

        try:
            serializerContact = ContactsSerializers(data=request.data)
            if serializerContact.is_valid():
                serializerContact.save()
                return Response(
                    {
                        'success': 'Heey! Ação efetuado acom sucesso.',
                        'status': True
                    },
                    status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! Houve um erro na atualização dos dados. Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):

        if not request.user.has_perm('users.update_contact'):
            return Response(
                {
                    'msm':
                    'Sem permissão de atualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        try:
            contact = Contact.objects.get(
                id=request.data["contact_id"],
                company_id=request.data["company_id"],
                user_id=request.data["user_id"],
                main=1,
                is_active=1)
            serializerContact = ContactsSerializers(contact, data=request.data)
            if serializerContact.is_valid():
                serializerContact.save()
                return Response(
                    {
                        'success': 'Heey! Ação efetuado acom sucesso.',
                        'status': True
                    },
                    status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! Houve um erro na atualização dos dados.  Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]
