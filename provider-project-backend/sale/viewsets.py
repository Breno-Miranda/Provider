from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User

from .models import Payment_form, Flags_card, Accrediting, Nature_operation, Sale

from .serializers import PaymentFormSerializers, FlagsCardSerializers, AccreditingSerializers, NatureOperationSerializers, SaleSerializers

# get method request
from request.serializers import ItensSerializers, RequestSerializers
# get method user 
from users.serializers import BusinesUsersSerializers, IndividualUsersSerializers
# grt method user model
from users.models import Busines, Individual

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from core import pagination

import io
from django.db.models import Q
from django.db.models.functions import Coalesce


from rest_framework.renderers import JSONRenderer

from datetime import datetime


class PaymentFormViewSet(ModelViewSet):
    queryset = Payment_form.objects.all()
    serializer_class = PaymentFormSerializers

class FlagsCardViewSet(ModelViewSet):
    queryset = Flags_card.objects.all()
    serializer_class = FlagsCardSerializers

class AccreditingViewSet(ModelViewSet):
    queryset = Accrediting.objects.all()
    serializer_class = AccreditingSerializers

class NatureOperationViewSet(ModelViewSet):
    queryset = Nature_operation.objects.all()
    serializer_class = NatureOperationSerializers

class SaleViewSet(viewsets.ViewSet):
 
    def list(self, request):

        requestId = request.GET.get('request_id', None)
        companyId = request.GET.get('company_id', None)
        actionSelect = request.GET.get('select', None)
        data_inicial = request.GET.get('data_inicial', datetime.today())
        data_final = request.GET.get('data_final', datetime.today())
        
        if companyId is None:
        	return Response({"erro": "Campo de vinculo com a empresa não foi enviado. retorno o codigo da empresa. ","status": False}, status=HTTP_404_NOT_FOUND)
       
        queryset = SaleSerializers(Sale.objects.all().filter(Q(company_id=companyId) | Q(request_id=requestId) | Q(date_register__range=(data_inicial, data_final))).order_by('-request_id'), many=True)
        
        if actionSelect is None:
       
            paginator = pagination.CustomPagination()
            page = paginator.paginate_queryset(queryset.data, request)
            if page is not None:
                return paginator.get_paginated_response(page)
            
        else:
            
            PaymentFormQueryset = PaymentFormSerializers(Payment_form.objects.all(), many=True)
            FlagsCardQueryset = FlagsCardSerializers(Flags_card.objects.all(), many=True)
            AccreditingQueryset = AccreditingSerializers(Accrediting.objects.all(), many=True)
            NatureOperationQueryset = NatureOperationSerializers(Nature_operation.objects.all(), many=True)
            
            queryset = {
                "selects":{
                    "payment_form": PaymentFormQueryset.data,
                    "flags_card": FlagsCardQueryset.data,
                    "accreditionting": AccreditingQueryset.data,
                    "nature_operation": NatureOperationQueryset.data,
                    "model_type": [ 
                         {"number": 1, "type":"NF-e" },
                         {"number": 2, "type":"NFC-e" }
                    ]
                }
            }
        if not queryset:
            return Response({"erro": "Não há registro.","status": False}, status=HTTP_404_NOT_FOUND) 

        return Response(queryset, status=HTTP_200_OK)

    def create(self , request):
        
        if not request.data:
            return Response({'msm': 'Campos vazios, preencha os obrigatorios.', 'status': 'danger'}, status=HTTP_404_NOT_FOUND)

        if request.data['customers']['is_type'] == 0: # cliente fisica
            
            dataCustomes = {
                "company": request.data['sale']['company_id'], 
                "user":request.data['sale']['user_id'],
                'name': request.data['customers']['name'],
                'cpf': request.data['customers']['cpf'],
                'number': request.data['customers']['number'],
                'address': request.data['customers']['address'],
                'is_active': 1,
            }

            print(dataCustomes)
            
            serializerIndividual = IndividualUsersSerializers(data=dataCustomes)
            print(serializerIndividual.is_valid())
            if serializerIndividual.is_valid():
                IndividualObj = serializerIndividual.save()
                idInididual = IndividualObj.id
                
        if request.data['customers']['is_type'] == 1: # cliente juridica
            
            dataCustomes = {
                "company": request.data['sale']['company_id'], 
                "user":request.data['sale']['user_id'],
                'company_name': request.data['customers']['company_name'],
                'cnpj': request.data['customers']['cnpj'],
                'number': request.data['customers']['number'],
                'address': request.data['customers']['address'],
                'state_registration': request.data['customers']['state_registration'],
                'municipal_registration': request.data['customers']['municipal_registration'],
                'is_active': 1,
            }
            
            serializerBusiness = BusinesUsersSerializers(data=dataCustomes)
            print(serializerBusiness.is_valid())
            if serializerBusiness.is_valid():
                BusinessObj = serializerBusiness.save()
                idBusiness = BusinessObj.id
                
        if request.data['customers']['is_type'] == 2:
            idInididual = ''
            idBusiness = ''
        else:
            idInididual = ''
            idBusiness = ''
            
        return Response( request.data['customers'])
            
        dataRequest = {
            "company": request.data['sale']['company_id'],
            "user": request.data['sale']['user_id'],
            "individual":idInididual and idInididual or '',
            "business": idBusiness and idBusiness or '',
            "status": '',
            "discount": request.data['sale']['discount'] and request.data['sale']['discount'] or 0,
            "subtotal": request.data['sale']['subtotal'] and request.data['sale']['subtotal'] or 0,
            "total": request.data['sale']['total'] and request.data['sale']['total'] or 0,
            "freight": request.data['sale']['freight'] and request.data['sale']['freight'] or 0,
            "amount":  request.data['sale']['amount'] and request.data['sale']['amount'] or 0,
            "observation": request.data['customers']['observation'] and request.data['customers']['observation'] or ''
        }
       
        serializerRequest = RequestSerializers(data=dataRequest)
        if serializerRequest.is_valid():
            requestObj = serializerRequest.save()
            
            for item in request.data['itens']:
                item["request"] = requestObj.id
        
            serializerItens = ItensSerializers(data=request.data['itens'], many=True)
            if serializerItens.is_valid():
                serializerItens.save()
            
                dataSale = {
                    "company": request.data['sale']['company_id'],
                    "user": request.data['sale']['user_id'],
                    "request": requestObj.id,
                    "individual":'',
                    "business":'',
                    "status":'',
                    "nature_operation": '',
                    "flags_card": '',
                    "payment_form": '',
                    "payment_form_amount": 0,
                    "accrediting": '',
                    "nsu_authorization": 0,
                    "discount": request.data['sale']['discount'],
                    "subtotal": request.data['sale']['subtotal'],
                    "total": request.data['sale']['total'],
                    "freight": request.data['sale']['freight'],
                    "amount": 0,
                    "change": request.data['sale']['change'],
                }
                
                serializerSale = SaleSerializers(data=dataSale)
                if serializerSale.is_valid():
                    SaleObj = serializerSale.save()
                    
                    return Response({'msm': 'Venda finalizada com sucesso.', 'idSale': SaleObj.id , 'idRequest': requestObj.id, 'status': 'success'},status=HTTP_200_OK)

        return Response({'msm': 'Não foi possivel criar venda.', 'status': 'danger'},status=HTTP_404_NOT_FOUND) 

    def update(self , request):

        if not request.data:
            return Response({'msm': 'Campos vazios, preencha os obrigatorios.', 'status': 'danger'},status=HTTP_404_NOT_FOUND) 

        serializer = SaleSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.update()
            return  Response({'msm': 'Registro atualizado com sucesso.', 'status': 'success'},status=HTTP_200_OK)
        return  Response({'msm': 'Error ao atualizar resgistro, certifique-se se tudo ocorreu como o correto e tente novamente.', 'status': False},status=HTTP_404_NOT_FOUND) 
