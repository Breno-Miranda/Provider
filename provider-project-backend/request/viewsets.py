from rest_framework.viewsets import ModelViewSet

from .models import Status, Request, Itens
from .serializers import ItensSerializers, RequestSerializers, StatusSerializers, requestCreateSerializers, requestItensCreateSerializers

from core import pagination

from django.db.models import Q
from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)


from campaign.models import Campaign
from company.models import Catalog
from lote.models import Lote
from users.models import Profile

from campaign.serializers import CampaignSerializers
from company.serializers import CatalogCompanySerializer
from lote.serializers import LotsSerializers
from users.serializers import UserBindProfileSerializers

class RequestViewSet(viewsets.ViewSet):
    

    def list(self, request):

        requestId = request.GET.get('request_id', None)
        companyId = request.GET.get('company_id', None)
        type_code = request.GET.get('type_code', None)
        _pagination = request.GET.get('pagination', None)
    
        if _pagination:
            
            queryset = RequestSerializers(Request.objects.all().filter(Q(company_id=companyId) | Q(id=requestId)).order_by('-id'), many=True)
        
            paginator = pagination.CustomPagination()
            page = paginator.paginate_queryset(queryset.data, request)
            if page is not None:
                return paginator.get_paginated_response(page)
                        
        if type_code:
            
            queryset_catalog = CatalogCompanySerializer(Catalog.objects.all().filter(company_id=companyId), many=True)
            queryset_campaign = CampaignSerializers(Campaign.objects.all().filter(company_id=companyId), many=True)
            queryset_lote = LotsSerializers(Lote.objects.all().filter(company_id=companyId), many=True)
            queryset_userBind = UserBindProfileSerializers(Profile.objects.all().filter(company_id=companyId , bind__type__code=type_code), many=True)

            queryset = {
            'catalogs': queryset_catalog.data,
            'campaigns': queryset_campaign.data,
            'lots': queryset_lote.data,
            'users': queryset_userBind.data,
            }

            return Response(queryset, status=HTTP_200_OK)
        
    def create(self, request):

        if not request.data:
            return Response(
                {
                    'error': 'Campos vazios, preencha os obrigatorios.',
                    'status': False
                },
                status=HTTP_404_NOT_FOUND)

        try:
            request_serializer = requestCreateSerializers(data=request.data)
            if request_serializer.is_valid():
                objRequets = request_serializer.save()

                for itens in request.data['itens']:
                    itens['request'] = objRequets.id

                request_itens_serializer = requestItensCreateSerializers(
                    data=request.data['itens'], many=True)
                if request_itens_serializer.is_valid():
                    request_itens_serializer.save()

                    return Response(
                        {
                            'success': 'Registro criado com sucesso.',
                            'status': True
                        },
                        status=HTTP_200_OK)
        except:
            return Response(
                {
                    'error':
                    'Error ao criar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.',
                    'status': False
                },
                status=HTTP_404_NOT_FOUND)

    def update(self, request):

        if not request.data:
            return Response(
                {
                    'error': 'Campos vazios, preencha os obrigatorios.',
                    'status': False
                },
                status=HTTP_404_NOT_FOUND)

        serializer = RequestSerializers(data=request.data)

        if serializer.is_valid():
            serializer.update()
            return Response(
                {
                    'success': 'Registro atualizado com sucesso.',
                    'status': True
                },
                status=HTTP_200_OK)
        return Response(
            {
                'error':
                'Error ao atualizar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.',
                'status': False
            },
            status=HTTP_404_NOT_FOUND)


class StatusViewSet(viewsets.ViewSet):
    def list(self, request):

        companyId = request.GET.get('company_id', None)

        queryset = StatusSerializers(
            Status.objects.all().filter(company_id=companyId), many=True)

        if not queryset:
            return Response({
                "erro": "Não há registro.",
                "status": False
            },
                            status=HTTP_404_NOT_FOUND)

        return Response(queryset, status=HTTP_200_OK)

    def create(self, request):

        if not request.data:
            return Response(
                {
                    'error': 'Campos vazios, preencha os obrigatorios.',
                    'status': False
                },
                status=HTTP_404_NOT_FOUND)

        serializer = StatusSerializers(data=request.data)

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

    def update(self, request):

        if not request.data:
            return Response(
                {
                    'error': 'Campos vazios, preencha os obrigatorios.',
                    'status': False
                },
                status=HTTP_404_NOT_FOUND)

        serializer = StatusSerializer(data=request.data)

        if serializer.is_valid():
            serializer.update()
            return Response(
                {
                    'success': 'Registro atualizado com sucesso.',
                    'status': True
                },
                status=HTTP_200_OK)
        return Response(
            {
                'error':
                'Error ao atualizar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.',
                'status': False
            },
            status=HTTP_404_NOT_FOUND)


class ItensViewSet(viewsets.ViewSet):
    def list(self, request):
        requestId = request.GET.get('request_id', None)
        companyId = request.GET.get('company_id', None)

        queryset = ItensSerializers(Itens.objects.all().filter(
            Q(company_id=companyId) & Q(request_id=requestId)),
                                    many=True)

        if not queryset:
            return Response({
                "erro": "Não há registro.",
                "status": False
            },
                            status=HTTP_404_NOT_FOUND)

        return Response(queryset, status=HTTP_200_OK)

    def create(self, request):

        if not request.data:
            return Response(
                {
                    'error': 'Campos vazios, preencha os obrigatorios.',
                    'status': False
                },
                status=HTTP_404_NOT_FOUND)

        serializer = ItensSerializers(data=request.data)

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

    def update(self, request):

        if not request.data:
            return Response(
                {
                    'error': 'Campos vazios, preencha os obrigatorios.',
                    'status': False
                },
                status=HTTP_404_NOT_FOUND)

        serializer = ItensSerializers(data=request.data)

        if serializer.is_valid():
            serializer.update()
            return Response(
                {
                    'success': 'Registro atualizado com sucesso.',
                    'status': True
                },
                status=HTTP_200_OK)
        return Response(
            {
                'error':
                'Error ao atualizar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.',
                'status': False
            },
            status=HTTP_404_NOT_FOUND)

# TODO: Colocar somattorio na tabela de pedido e itens do desconto e comissao
class requestsFromPdfViewSet(viewsets.ViewSet):
    
    def list(self, request):
        
        
        requestId = request.GET.get('request_id', None)
        companyId = request.GET.get('company_id', None)

        try:
            
            if not companyId:
                return Response({"error": "Obrigatorio a informação da empresa.","status": False},status=HTTP_404_NOT_FOUND)
            
            if not requestId:
                return Response({"error": "Obrigatorio a informação do pedido." ,"status": False},status=HTTP_404_NOT_FOUND)
            
            queryset = []

            queryset_requets = RequestSerializers(Request.objects.get(company=companyId , id=requestId))
            
            queryset_itens = ItensSerializers(Itens.objects.all().filter(request_id=requestId),many=True)
            
            queryset = dict()
            queryset.update(queryset_requets.data)
            queryset.update({'itens': queryset_itens.data})
            
            return Response(queryset, status=HTTP_200_OK)

        except:
            return Response({"error": "Aconteceu algum inesperado. Entre em contato com o suporte.", "status": False},status=HTTP_404_NOT_FOUND)

       
       


# criando função para conserto de valores totais dos pedidos.
class routineRequestsSumItensViewSet(viewsets.ViewSet):
    
    def list(self, request):
            
        companyId = request.GET.get('company_id', None)

        try:
            
            if not companyId:
                return Response({"error": "Obrigatorio a informação da empresa.","status": False},status=HTTP_404_NOT_FOUND)
            
            result = []
            
            result = Itens.objects.values('request').annotate(amount=Sum('total')).filter(request__company=companyId)
            
            for item in result:
                Request.objects.filter(pk=item['request']).update(amount=item['amount'])
            
            return Response({"success": "Os valores dos pedidos foram atualizados com sucesso.", "result": result}, status=HTTP_200_OK)

        except:
            return Response({"error": "Aconteceu algum inesperado. Entre em contato com o suporte.", "status": False},status=HTTP_404_NOT_FOUND)

       
