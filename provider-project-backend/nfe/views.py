
import io
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models.functions import Coalesce
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Biblioteca de comunicação http/https
import http.client
# Biblioteca para manipulação de json
import json


@api_view(['POST'])
def emit(request):
    if request.method == 'POST':
         # Converte o array em json novamente
        json = {
                "ID": 1137,
                "url_notificacao": "http://meudominio.com/retorno.php",
                "operacao": 1,
                "natureza_operacao": "Venda de produção do estabelecimento",
                "modelo": 1,
                "finalidade": 1,
                "ambiente": 2,
                "cliente": {
                    "cpf": "000.000.000-00",
                    "nome_completo": "Nome do Cliente",
                    "endereco": "Av. Brg. Faria Lima",
                    "complemento": "Escritório",
                    "numero": 1000,
                    "bairro": "Itaim Bibi",
                    "cidade": "São Paulo",
                    "uf": "SP",
                    "cep": "00000-000",
                    "telefone": "(00) 0000-0000",
                    "email": "nome@email.com"
                },
                "produtos": [
                    {
                        "nome": "Nome do produto",
                        "codigo": "nome-do-produto",
                        "ncm": "6109.10.00",
                        "cest": "28.038.00",
                        "quantidade": 3,
                        "unidade": "UN",
                        "peso": "0.800",
                        "origem": 0,
                        "subtotal": "44.90",
                        "total": "134.70",
                        "classe_imposto": "REF1000"
                    },
                    {
                        "nome": "Nome do produto",
                        "codigo": "nome-do-produto",
                        "ncm": "6109.10.00",
                        "cest": "28.038.00",
                        "quantidade": "1",
                        "unidade": "UN",
                        "peso": "0.200",
                        "origem": 0,
                        "subtotal": "29.90",
                        "total": "29.90",
                        "impostos": {
                        "icms": {
                            "codigo_cfop": "6.102",
                            "situacao_tributaria": "102"
                        },
                        "ipi": {
                            "situacao_tributaria": "99",
                            "codigo_enquadramento": "999",
                            "aliquota": "0.00"
                        },
                        "pis": {
                            "situacao_tributaria": "99",
                            "aliquota": "0.00"
                        },
                        "cofins": {
                            "situacao_tributaria": "99",
                            "aliquota": "0.00"
                        }
                        }
                    }
                ],
                "pedido": {
                    "pagamento": 0,
                    "presenca": 2,
                    "modalidade_frete": 0,
                    "frete": "12.56",
                    "desconto": "10.00",
                    "total": "174.60",
                    "forma_pagamento": 15
                }
                }
        
        #  Define o Host para a comunicação com a API
        conn = http.client.HTTPSConnection("webmaniabr.com")

        # Credenciais de acesso
        headers = {
            'cache-control': "no-cache",
            'content-type': "application/json",
            'x-consumer-key': "SEU_CONSUMER_KEY",
            'x-consumer-secret': "SEU_CONSUMER_SECRET",
            'x-access-token': "SEU_ACCESS_TOKEN",
            'x-access-token-secret': "SEU_ACCESS_TOKEN_SECRET"
        }

        # Comunicando com a API
        conn.request("POST", "/api/1/nfe/emissao/", json, headers)

        # Retorno da API
        res = conn.getresponse()
        data = res.read()

        # Exibir retorno
        print(data.decode("utf-8"))

def cancel(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})



        