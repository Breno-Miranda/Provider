from rest_framework.viewsets import ModelViewSet

from .models import Campaign
from .serializers import CampaignSerializers

from django.db.models import Q
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

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

class CampaignsViewset(viewsets.ViewSet):
 
    def list(self, request):
        
        companyId = request.GET.get('company_id', None)

        queryset = CampaignSerializers(Campaign.objects.all().filter(company_id=companyId), many=True)

        if not queryset:
                return Response({"erro": "Não há registro.","status": False}, status=HTTP_404_NOT_FOUND) 

        return Response(queryset.data, status=HTTP_200_OK)
    
    def create(self , request):
     
        if not request.data:
            return Response({'error': 'Campos vazios, preencha os obrigatorios.', 'status': False}, status=HTTP_404_NOT_FOUND) 

        serializer = CampaignSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Registro criado com sucesso.', 'status': True},status=HTTP_200_OK)
        return Response({'error': 'Error ao criar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.', 'status': False},status=HTTP_404_NOT_FOUND) 


    def update(self , request):

        if not request.data:
            return Response({'error': 'Campos vazios, preencha os obrigatorios.', 'status': False},status=HTTP_404_NOT_FOUND) 

        serializer = CampaignSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return  Response({'success': 'Registro atualizado com sucesso.', 'status': True},status=HTTP_200_OK)
        return  Response({'error': 'Error ao atualizar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.', 'status': False},status=HTTP_404_NOT_FOUND) 
    
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