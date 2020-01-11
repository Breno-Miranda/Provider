from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import Permission, Group, User

from users.models import  Busines, Individual, Collaborator, Bind
from users.serializers import BusinesUsersSerializers, IndividualUsersSerializers, ColaborationUsersSerializers

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
from rest_framework.permissions import  IsAuthenticated

class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_admin
    
class InfoSystemViewSet(viewsets.ViewSet):
 
    def list(self, request):
        
        try:
            
            companyId = request.GET.get('company_id', None)
            userId = request.GET.get('user_id', None)
            type_code = request.GET.get('type_code', None)
            is_business = request.GET.get('is_business', None)
            is_individual = request.GET.get('is_individual', None)
            is_collaborator = request.GET.get('is_collaborator', None)

            print(is_collaborator)
            
            if(is_collaborator):
                
                if(type_code == '1'):
                    
                    return Response( {
                        "collaborator": Bind.objects.filter(company=companyId,is_collaborator=1).count(),  
                        "individual": Bind.objects.filter(company=companyId,is_individual=1).count(), 
                        "busines": Bind.objects.filter(company=companyId,is_business=1).count(), 
                     },status=HTTP_200_OK)
                    
                elif(type_code == '2'):
                    
                    return Response( {
                        "collaborator": Collaborator.objects.filter(user_bond=userId).count(),  
                        "individual": Individual.objects.filter(user_bond=userId).count(), 
                        "busines": Busines.objects.filter(user_bond=userId).count(), 
                     },status=HTTP_200_OK)
                    
                else:
                    return Response({},status=HTTP_200_OK)
            else:
                return Response({},status=HTTP_200_OK)
        except:
            return Response({'msm':'API identificou um erro! verificar logica.' , 'status': 'danger' , 'return': True},status=status.HTTP_204_NO_CONTENT)
         
    def get_permissions(self):
        
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]
    
       
            
            