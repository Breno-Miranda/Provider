from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import Permission, Group, User
from users.models import Contact, Bank_Account, Busines, Individual, Collaborator, Profile, Bind
from .serializers import ContactsSerializers, BusinesUsersSerializers, IndividualUsersSerializers, ColaborationUsersSerializers, UsersSerializer, GroupSerializer, PermissionSerializer, UsersSerializer, UserBindSerializers, BankAccountUsersSerializers

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN,
                                   HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND,
                                   HTTP_200_OK)
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


class CollaboratorUsersViewSet(viewsets.ViewSet):
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
        user_id = request.GET.get('user_id', None)

        try:
            queryset_colaborator = ColaborationUsersSerializers(
                Collaborator.objects.get(company_id=companyId,
                                         user_id=user_id),
                context={"request": request})
            return Response(queryset_colaborator.data, status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! listagem validada e encontrada um error.  Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def create(self, request, pk):

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
            serializerCollaboration = ColaborationUsersSerializers(
                data=request.data)
            if serializerCollaboration.is_valid():
                serializerCollaboration.save()
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
                    "Oops! Houve um erro no cadastro.  Tente novamente...",
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
            collaborator = Collaborator.objects.get(
                id=pk,
                company_id=request.data["company_id"],
                user_id=request.data["user_id"])
            serializerCollaboration = ColaborationUsersSerializers(
                collaborator, data=request.data)
            if serializerCollaboration.is_valid():
                serializerCollaboration.save()

                if request.data['photo']:
                    collaborator.photo = request.data['photo']
                    collaborator.save()
                if request.data['anexo']:
                    collaborator.anexo = request.data['anexo']
                    collaborator.save()

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
                    "Oops! Houve um erro no atualização.  Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):

        if not request.user.has_perm('users.delete_profile'):
            return Response(
                {
                    'msm':
                    'Sem permissão de exclusão. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        try:
            collaborator = Collaborator.objects.get(
                id=pk,
                company_id=request.data["company_id"],
                user_id=request.data["user_id"])
            collaborator.is_active = request.data['is_active']
            collaborator.save()

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
                    "Oops! Houve um erro na exclusão.  Tente novamente...",
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


class IndividualViewSet(viewsets.ViewSet):
    def list(self, request):

        if not request.user.has_perm('users.view_individual'):
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
            queryset_individual = IndividualUsersSerializers(
                Individual.objects.get(user_id=user_id, company_id=companyId))
            return Response(queryset_individual.data, status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! Houve um erro na listagem dos dados.  Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def create(self, request):

        if not request.user.has_perm('users.create_bussines'):
            return Response(
                {
                    'msm':
                    'Sem permissão de criação. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        try:
            serializerIndividual = IndividualUsersSerializers(
                data=request.data)
            if serializerIndividual.is_valid():
                serializerIndividual.save()
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

        if not request.user.has_perm('users.update_bussines'):
            return Response(
                {
                    'msm':
                    'Sem permissão de atualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        try:
            individual = IndividualUsersSerializers(
                Individual.objects.get(id=pk,
                                       user_id=user_id,
                                       company_id=companyId))
            serializerIndividual = IndividualUsersSerializers(
                individual, data=request.data)
            if serializerIndividual.is_valid():
                serializerIndividual.save()
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

        if not request.user.has_perm('provider.delete_provider'):
            return Response(
                {
                    'msm':
                    'Sem permissão de exclusão. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)
        try:
            individual = IndividualUsersSerializers(
                Individual.objects.get(id=pk,
                                       user_id=user_id,
                                       company_id=companyId))
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


class BusinesViewSet(viewsets.ViewSet):
    def list(self, request):

        if not request.user.has_perm('users.view_bussines'):
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
            queryset_busines = BusinesUsersSerializers(
                Busines.objects.get(user_id=user_id, company_id=companyId))
            return Response(queryset_busines.data, status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm':
                    "Oops! Houve um erro na listagem dos dados.  Tente novamente...",
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def create(self, request):

        if not request.user.has_perm('users.create_bussines'):
            return Response(
                {
                    'msm':
                    'Sem permissão de criação. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_400_BAD_REQUEST)

        try:
            serializerBusiness = BusinesUsersSerializers(data=request.data)
            if serializerBusiness.is_valid():
                serializerBusiness.save()
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

    def update(self, request, pk=None):

        if not request.user.has_perm('users.update_bussines'):
            return Response(
                {
                    'msm':
                    'Sem permissão de atualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        if not request.user.has_perm('provider.delete_provider'):
            return Response(
                {
                    'msm':
                    'Sem permissão de exclusão. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_400_BAD_REQUEST)
        try:
            queryset_busines = BusinesUsersSerializers(
                Busines.objects.get(id=pk,
                                    user_id=user_id,
                                    company_id=companyId))
        except:
            pass

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


class PermissionViewSet(viewsets.ViewSet):
    def list(self, request):

        if not request.user.has_perm('users.view_permission'):
            return Response(
                {
                    'msm':
                    'Sem permissão de visualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        try:
            querysetPermission = PermissionSerializer(Permission.objects.all(),
                                                      many=True)
            queryset = {"permission": querysetPermission.data}
            return Response(queryset, status=HTTP_200_OK)
        except:
            return Response(
                {
                    'msm': 'Não perfil cadastrado',
                    'status': 'danger'
                },
                status=HTTP_404_NOT_FOUND)

    def create(self, request):

        try:
            if not request.user.has_perm('users.add_permission'):
                return Response(
                    {
                        'msm':
                        'Sem permissão de criação. Você será redirecionad(a) para pagina principal.',
                        'status': 'danger',
                        'return': True
                    },
                    status=HTTP_400_BAD_REQUEST)

            if not request.data:
                return Response(
                    {
                        'error': 'Selecione as permissions necessarias.',
                        'status': False
                    },
                    status=HTTP_404_NOT_FOUND)

            for p in request.data['obj_permission']:
                users = User.objects.get(pk=p['user_id'])
                permission = Permission.objects.get(pk=p['permission_id'])
                users.user_permissions.add(permission)

            for p in request.data['obj_permission_delete']:
                users = User.objects.get(pk=p['user_id'])
                permission = Permission.objects.get(pk=p['permission_id'])
                users.user_permissions.remove(permission)

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

        if not request.user.has_perm('users.view_bussines'):
            return Response(
                {
                    'msm':
                    'Sem permissão de visualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_403_FORBIDDEN)

        try:
            queryset = UserBindSerializers(Bind.objects.all(),
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

    def create(self, request):

        if not request.user.has_perm('users.create_bussines'):
            return Response(
                {
                    'msm':
                    'Sem permissão de criação. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_400_BAD_REQUEST)

        if not request.data:
            return Response(
                {
                    'error': 'Campos vazios, preencha os obrigatorios.',
                    'status': False
                },
                status=HTTP_404_NOT_FOUND)

        serializer = BusinesUsersSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'success': 'Registro criado com sucesso.',
                    'status': True
                },
                status=HTTP_200_OK)
        return Response(
            {
                'error':
                'Error ao criar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.',
                'status': False
            },
            status=HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):

        if not request.user.has_perm('users.update_bussines'):
            return Response(
                {
                    'msm':
                    'Sem permissão de atualização. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_400_BAD_REQUEST)

        serializer = BusinesUsersSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'success': 'Registro criado com sucesso.',
                    'status': True
                },
                status=HTTP_200_OK)
        return Response(
            {
                'error':
                'Error ao criar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.',
                'status': False
            },
            status=HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):

        if not request.user.has_perm('provider.delete_provider'):
            return Response(
                {
                    'msm':
                    'Sem permissão de exclusão. Você será redirecionad(a) para pagina principal.',
                    'status': 'danger',
                    'return': True
                },
                status=HTTP_400_BAD_REQUEST)
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(
            {
                'msm': 'Exclusão efetuada com sucessso!',
                'status': 'success',
                'return': True
            },
            status=status.HTTP_204_NO_CONTENT)

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

        if not request.user.has_perm('users.add_bank_account'):
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

        if not request.user.has_perm('users.change_bank_account'):
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


# USER FORGOTTHEPASSOWORD ENDPOINT
# class ForgotThePasswordUsersViewSet(ModelViewSet):

#     serializer_class = UsersSerializer

#     def get_queryset(self):
#         queryset = User.objects.all()
#         email = self.request.query_params.get('email', None)
#         if email is not None:
#             queryset = queryset.filter(email=email)
#         return queryset


