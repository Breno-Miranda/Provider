from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework import generics
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes

# Serializers
from users.serializers import UserBindSerializers, ProfileSerializers
from company.serializers import CompanyKeySecretSerializer, CompanyKeySimplesSerializer
# Models
from django.contrib.auth.models import User
from users.models import Bind, Profile
from company.models import Company, Key

import os
import binascii
import jwt
import json

class Authentication(generics.ListCreateAPIView):
    
    @csrf_exempt
    @api_view(["POST"])
    @permission_classes((AllowAny,))
    def auth(request):
        
        username = request.data.get("username")
        password = request.data.get("password")
        bind = request.data.get("bind")
        
        try:
            
            if not bind:
                return Response({'error': 'Erro ! Usuario não foi vinculado a nenhuma empresa. Tente novamente.', 'status': False}, status=HTTP_400_BAD_REQUEST)
            
            if username is None or password is None:
                return Response({'error': 'Por favor, insira um usuário e senha corretos para uma conta da empresa a estar vinculada. Note que ambos campos são sensíveis a maiúsculas e minúsculas.', 'status': False}, status=HTTP_400_BAD_REQUEST)
        
            user = authenticate(username=username, password=password)
            
            if not user:
                return Response({'error': 'Credenciais não existe ou não estar ativa. Por favor, insira um usuário e senha corretos para uma conta da empresa a estar vinculada. Note que ambos campos são sensíveis a maiúsculas e minúsculas.', 'status': False},status=HTTP_404_NOT_FOUND)
        
            token, _ = Token.objects.get_or_create(user=user)
            
            return Response({
                        'token': token.key,
                        
                        'id': user.id,
                        'email': user.email,
                        'bindId': bind['id'],
                        'last_name': user.last_name,
                        'first_name': user.first_name,
                        'companyId': bind['_company']['id'],
                        
                        'color_primary': bind['_company']['color_primary'],
                        'color_secudary': bind['_company']['color_secudary'],
                        
                        'type': bind['_type']['type'],
                        'team': bind['_team']['name'],
                        'sector': bind['_sector']['name'],
                        'type_code': bind['_type']['code'],
                      
                        'cnpj': bind['_company']['cnpj'],
                        'logo': bind['_company']['logo'],
                        'website': bind['_company']['website'],
                        'name_company': bind['_company']['name_company'],
                            
                        'is_collaborator': bind['is_collaborator'],
                        'is_business': bind['is_business'],
                        'is_individual': bind['is_individual']},
                            
            status=HTTP_200_OK) 
            
        except:
            return Response({'error': 'Erro na autenticação. Tente novamente, caso ocorra novamente entre em contato com o suporte técnico.', 'status': False},status=HTTP_404_NOT_FOUND)
       
    
    @csrf_exempt
    @api_view(["POST"])
    @permission_classes((AllowAny,))
    def check_auth(request):
        
        username = request.data.get("username")
        password = request.data.get("password")
        
        try:
        
            if username is None or password is None:
                return Response({'error': 'Por favor, insira um usuário e senha corretos para uma conta da empresa a estar vinculada. Note que ambos campos são sensíveis a maiúsculas e minúsculas.', 'status': False}, status=HTTP_400_BAD_REQUEST)
            
            user = authenticate(username=username, password=password)
            
            if not user:
                return Response({'error': 'Credenciais não existe ou não estar ativa. Por favor, insira um usuário e senha corretos para uma conta da empresa a estar vinculada. Note que ambos campos são sensíveis a maiúsculas e minúsculas.', 'status': False},status=HTTP_404_NOT_FOUND)
            
            user = Bind.objects.all().filter(user=user)
            
            if not user:
                return Response({'error': 'Seu usuario não estar vinculado a nenhuma empresa. Entre em contato com suporte.', 'status': False},status=HTTP_404_NOT_FOUND)

            user = UserBindSerializers(user, many=True , context={"request": request})
            return Response({'user': user.data, 'status': True}, status=HTTP_200_OK) 
        
        except:
            return Response({'error': 'Credenciais não existe. Por favor, insira um usuário e senha corretos para uma conta da empresa a estar vinculada. Note que ambos campos são sensíveis a maiúsculas e minúsculas.', 'status': False},status=HTTP_404_NOT_FOUND)
        
    @csrf_exempt
    @api_view(["POST"])
    @permission_classes((AllowAny,))
    def register_user_token(request):
        
        token = request.data.get('token')
     
        if token:
            decoded_simples = jwt.decode(token, 'ZTkXVpBwEkW4S32roccJKg==', algorithms='HS256')
            if decoded_simples:
                return Response(decoded_simples, status=HTTP_200_OK) 
        else:
            return Response({'error': 'Não foi localizado as simples chave de empresa que desejas se vincular.', 'status': False},status=HTTP_404_NOT_FOUND)
    @csrf_exempt
    @api_view(["POST"])
    @permission_classes((AllowAny,))
    def company_token(request):
        
        token = request.data.get('token')
     
        if token:
            decoded_simples = jwt.decode(token, 'ZTkXVpBwEkW4S32roccJKg==', algorithms='HS256')
            if decoded_simples:
                company = CompanyKeySimplesSerializer(Company.objects.get(id=decoded_simples['id']), context={"request": request} )
                return Response(company.data, status=HTTP_200_OK) 
        else:
            return Response({'error': 'Não foi localizado as simples chave de empresa que desejas se vincular.', 'status': False},status=HTTP_404_NOT_FOUND)
        