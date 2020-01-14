
from .models import Company, Catalog
from .serializers import CompanySerializer, CatalogCompanySerializer

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
    
class CompanyViewSet(viewsets.ViewSet):
    
    def list(self, request):
    
        if not request.user.has_perm('company.view_company'):
            return Response({'msm':'Sem permissão de visualização. Você será redirecionad(a) para pagina principal.' , 'status': 'danger' , 'return': True},status=HTTP_400_BAD_REQUEST) 
        
        companyId = request.GET.get('company_id', None)
        
        try:
            queryset = CompanySerializer(Company.objects.get(company_id=companyId), context={"request": request})
            return Response(queryset.data,status=HTTP_200_OK)
        except:
            return Response({'msm':'Não perfil cadastrado' , 'status': 'danger'},status=HTTP_404_NOT_FOUND) 

    def create(self, request):
        
        if not request.user.has_perm('company.update_company'):
            return Response({'msm':'Sem permissão de atualização. Você será redirecionad(a) para pagina principal.' , 'status': 'danger' , 'return': True},status=HTTP_400_BAD_REQUEST) 

        serializer = CompanySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return  Response({'msm': 'Produto cadastrado com sucesso.', 'status': 'success'},status=HTTP_200_OK)
        
        return  Response({'msm': 'Error ao cadastrar, certifique se preencheu todos os campos.', 'status': 'danger'},status=HTTP_404_NOT_FOUND) 
    
    def update(self, request, pk=None):
        
        if not request.user.has_perm('company.update_company'):
            return Response({'msm':'Sem permissão de atualização. Você será redirecionad(a) para pagina principal.' , 'status': 'danger' , 'return': True},status=HTTP_400_BAD_REQUEST) 

        serializer = CompanySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return  Response({'msm': 'Produto cadastrado com sucesso.', 'status': 'success'},status=HTTP_200_OK)
        
        return  Response({'msm': 'Error ao cadastrar, certifique se preencheu todos os campos.', 'status': 'danger'},status=HTTP_404_NOT_FOUND) 
    
    def get_permissions(self):
        
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]
    
    
    
class CatalogsCompanyViewSet(viewsets.ViewSet):
    
    def list(self, request):
    
        if not request.user.has_perm('company.view_company'):
            return Response({'msm':'Sem permissão de visualização. Você será redirecionad(a) para pagina principal.' , 'status': 'danger' , 'return': True},status=HTTP_400_BAD_REQUEST) 
        
        companyId = request.GET.get('company_id', None)
        
        try:
            queryset = CatalogCompanySerializer(Catalog.objects.all().filter(company_id=companyId),many=True, context={"request": request})
            return Response(queryset.data,status=HTTP_200_OK)
        except:
            return Response({'msm':'Não perfil cadastrado' , 'status': 'danger'},status=HTTP_404_NOT_FOUND) 


    def create(self, request):
        
        if not request.user.has_perm('company.update_company'):
            return Response({'msm':'Sem permissão de atualização. Você será redirecionad(a) para pagina principal.' , 'status': 'danger' , 'return': True},status=HTTP_400_BAD_REQUEST) 

        serializer = CatalogCompanySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return  Response({'msm': 'Produto cadastrado com sucesso.', 'status': 'success'},status=HTTP_200_OK)
        
        return  Response({'msm': 'Error ao cadastrar, certifique se preencheu todos os campos.', 'status': 'danger'},status=HTTP_404_NOT_FOUND) 
    
    def update(self, request, pk=None):
        
        if not request.user.has_perm('company.update_company'):
            return Response({'msm':'Sem permissão de atualização. Você será redirecionad(a) para pagina principal.' , 'status': 'danger' , 'return': True},status=HTTP_400_BAD_REQUEST) 

        serializer = CatalogCompanySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return  Response({'msm': 'Produto cadastrado com sucesso.', 'status': 'success'},status=HTTP_200_OK)
        
        return  Response({'msm': 'Error ao cadastrar, certifique se preencheu todos os campos.', 'status': 'danger'},status=HTTP_404_NOT_FOUND) 
    
    def get_permissions(self):
        
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]