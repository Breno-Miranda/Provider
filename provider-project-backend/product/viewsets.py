from rest_framework.viewsets import ModelViewSet
from .models import Product, Status, Category

from .serializers import ProductSerializer , ProductNewSerializer,  CategorySerializer , StatusSerializer

# taxation
from taxation.serializers import TaxSerializer
from taxation.models import Tax

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from core import pagination

from django.db.models import Q

class ProductViewSet(viewsets.ViewSet):

    # TODO: O CAMPO COMPANY ID DEVE SER OPCIONAL, FAZER A BUSCAR TBM PELO CATALOGO_COMPANY OBRIGATORIO
    def list(self, request):
        companyId = request.GET.get('company_id', None)
        _pagination = request.GET.get('pagination', None)
        _limit = request.GET.get('limit', None)
        _search = request.GET.get('search', None)
         
        
        if _limit is not None:
            if _search is not None:
                products = Product.objects.all().filter(Q(company_id=companyId) & Q(reference=_search) )[:int(_limit)]

            else:
                products = ProductSerializer(Product.objects.all().filter(company_id=companyId)[:int(_limit)], many=True)

        else:
            if _search is not None:
                products = ProductSerializer(Product.objects.get(Q(company_id=companyId) & Q(reference=_search) ))
            else:
                products = ProductSerializer(Product.objects.all().filter(company_id=companyId), many=True)
  
            
        if _pagination is not None:
            paginator = pagination.CustomPagination()
            page = paginator.paginate_queryset(products.data, request)
            if page is not None:
                return paginator.get_paginated_response(page)
            
        return Response({'results': products.data, 'status': True},status=HTTP_200_OK)

    
class NewProductViewSet(viewsets.ViewSet):
    
    def list(self, request):
        
        companyId = request.GET.get('company_id', None)
      
        category = CategorySerializer(Category.objects.all().filter(company_id=companyId), many=True)
        status = StatusSerializer(Status.objects.all().filter(company_id=companyId), many=True)
        tax = TaxSerializer(Tax.objects.all().filter(company_id=companyId), many=True)
                
        queryset = {
            "selects":{
                "status": status.data,
                "category": category.data,
                "tax": tax.data,
            }
        }
        
        if not queryset:
            return  Response({'msm': 'consulta vazia.', 'status': 'danger'},status=HTTP_404_NOT_FOUND) 
        
        return Response(queryset)

    def create(self, request):
        
        if not request.data:
            return  Response({'msm': 'Campos obrigatorios não preenchido.', 'status': 'danger'},status=HTTP_404_NOT_FOUND) 
        
        serializer = ProductNewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return  Response({'msm': 'Produto cadastrado com sucesso.', 'status': 'success'},status=HTTP_200_OK)
        
        return  Response({'msm': 'Error ao cadastrar, certifique se preencheu todos os campos.', 'status': 'danger'},status=HTTP_404_NOT_FOUND) 

