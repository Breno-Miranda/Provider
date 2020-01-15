from rest_framework.viewsets import ModelViewSet

from .models import Status, Request, Itens
from .serializers import ItensSerializers, RequestSerializers, StatusSerializers, requestCreateSerializers, requestItensCreateSerializers

from core import pagination
from django.db.models import Q
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

class RequestViewSet(viewsets.ViewSet):
 
    def list(self, request):
        
        requestId = request.GET.get('request_id', None)
        companyId = request.GET.get('company_id', None)

        querysetRequest = RequestSerializers(Request.objects.all().filter(Q(company_id=companyId) | Q(id=requestId) ), many=True)


        if not querysetRequest:
                return Response({"erro": "Não há registro.","status": False}, status=HTTP_404_NOT_FOUND) 

        return Response(querysetRequest.data, status=HTTP_200_OK)
    
    def create(self , request):
     
        if not request.data:
            return Response({'error': 'Campos vazios, preencha os obrigatorios.', 'status': False}, status=HTTP_404_NOT_FOUND) 

        request_serializer = requestCreateSerializers(data=request.data)
        if request_serializer.is_valid():
            objRequets = request_serializer.save()
            
            for itens in request.data['itens']:
                itens['request'] = objRequets.id
                
            print(request.data['itens'])   
            request_itens_serializer = requestItensCreateSerializers(data=request.data['itens'], many=True)
            # print(request.data['itens'])
            print(request_itens_serializer.is_valid())
            # print(request_itens_serializer)
            if request_itens_serializer.is_valid():
                request_itens_serializer.save()
            
            
            
        #     return Response({'success': 'Registro criado com sucesso.', 'status': True},status=HTTP_200_OK)
        # return Response({'error': 'Error ao criar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.', 'status': False},status=HTTP_404_NOT_FOUND) 
        pass
        return Response({'success':  request.data, 'status': True},status=HTTP_200_OK)

    def update(self , request):

        if not request.data:
            return Response({'error': 'Campos vazios, preencha os obrigatorios.', 'status': False},status=HTTP_404_NOT_FOUND) 

        serializer = RequestSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.update()
            return  Response({'success': 'Registro atualizado com sucesso.', 'status': True},status=HTTP_200_OK)
        return  Response({'error': 'Error ao atualizar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.', 'status': False},status=HTTP_404_NOT_FOUND) 
    
    
    
class StatusViewSet(viewsets.ViewSet):
 
    def list(self, request):
        
        companyId = request.GET.get('company_id', None)
        
        queryset = StatusSerializers(Status.objects.all().filter(company_id=companyId), many=True)
        
        if not queryset:
                return Response({"erro": "Não há registro.","status": False}, status=HTTP_404_NOT_FOUND) 

        return Response(queryset, status=HTTP_200_OK)
    
    def create(self , request):
     
        if not request.data:
            return Response({'error': 'Campos vazios, preencha os obrigatorios.', 'status': False}, status=HTTP_404_NOT_FOUND) 

        serializer = StatusSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Registro criado com sucesso.', 'status': True},status=HTTP_200_OK)
        return Response({'error': 'Error ao criar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.', 'status': False},status=HTTP_404_NOT_FOUND) 


    def update(self , request):

        if not request.data:
            return Response({'error': 'Campos vazios, preencha os obrigatorios.', 'status': False},status=HTTP_404_NOT_FOUND) 

        serializer = StatusSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.update()
            return  Response({'success': 'Registro atualizado com sucesso.', 'status': True},status=HTTP_200_OK)
        return  Response({'error': 'Error ao atualizar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.', 'status': False},status=HTTP_404_NOT_FOUND) 
    

class ItensViewSet(viewsets.ViewSet):
 
    def list(self, request):
        requestId = request.GET.get('request_id', None)
        companyId = request.GET.get('company_id', None)
        
        queryset = ItensSerializers(Itens.objects.all().filter(Q(company_id=companyId) & Q(request_id=requestId)), many=True)
        
        if not queryset:
                return Response({"erro": "Não há registro.","status": False}, status=HTTP_404_NOT_FOUND) 

        return Response(queryset, status=HTTP_200_OK)
    
    def create(self , request):
     
        if not request.data:
            return Response({'error': 'Campos vazios, preencha os obrigatorios.', 'status': False}, status=HTTP_404_NOT_FOUND) 

        serializer = ItensSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Registro criado com sucesso.', 'status': True},status=HTTP_200_OK)
        return Response({'error': 'Error ao criar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.', 'status': False},status=HTTP_404_NOT_FOUND) 


    def update(self , request):

        if not request.data:
            return Response({'error': 'Campos vazios, preencha os obrigatorios.', 'status': False},status=HTTP_404_NOT_FOUND) 

        serializer = ItensSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.update()
            return  Response({'success': 'Registro atualizado com sucesso.', 'status': True},status=HTTP_200_OK)
        return  Response({'error': 'Error ao atualizar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.', 'status': False},status=HTTP_404_NOT_FOUND) 
    
