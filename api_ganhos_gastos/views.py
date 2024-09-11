import io
import datetime
from .serializers import ExtratoSerializer
from api_ganhos_gastos.models import Gastos, Ganhos, Extrato, GastosFixos, GastosTemporarios
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework import viewsets

class ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer

#gastos

def registrar_gastos(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        nome = listaDeValores[0]
        categoria = listaDeValores[1]
        valor = listaDeValores[2]
        pagamento = listaDeValores[3]
        banco = listaDeValores[4]
        id = listaDeValores[5]
         
        gasto = Gastos.objects.create(
            nome = nome,
            categoria = categoria,
            valor = valor,
            pagamento = pagamento,
            banco = banco,
            dono_id = id
        )

        gasto.save()
        data = {
            'status': 'gasto registrada'
        }
        return JsonResponse(data)

def editar_gastos(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        nome = listaDeValores[0]
        categoria = listaDeValores[1]
        valor = listaDeValores[2]
        pagamento = listaDeValores[3]
        banco = listaDeValores[4]
        id = listaDeValores[5]

        gastosdb = Gastos.objects.get(pk = id)
        gastosdb.nome = nome
        gastosdb.categoria = categoria
        gastosdb.valor = valor
        gastosdb.pagamento = pagamento
        gastosdb.banco = banco

        gastosdb.save()

        data2 = {
            'status': 'gasto editado'
        }
    return JsonResponse(data2)

#ganhos

def registrar_ganhos(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        nome = listaDeValores[0]
        categoria = listaDeValores[1]
        valor = listaDeValores[2]
        banco = listaDeValores[3]
        id = listaDeValores[4]
         
        ganho = Ganhos.objects.create(
            nome = nome,
            categoria = categoria,
            valor = valor,
            banco = banco,
            dono_id = id
        )

        ganho.save()
        data = {
            'status': 'ganho registrada'
        }
        return JsonResponse(data)

def editar_ganhos(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        nome = listaDeValores[0]
        categoria = listaDeValores[1]
        valor = listaDeValores[2]
        banco = listaDeValores[3]
        id = listaDeValores[4]

        ganhosdb = Ganhos.objects.get(pk = id)
        ganhosdb.nome = nome
        ganhosdb.categoria = categoria
        ganhosdb.valor = valor
        ganhosdb.banco = banco

        ganhosdb.save()

        data2 = {
            'status': 'gasto editado'
        }
    return JsonResponse(data2)

#extrato

def Registrar_extrato(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        nome = listaDeValores[0]
        valor = listaDeValores[1]
        ganho_gasto = listaDeValores[2]
        id = listaDeValores[3]
         
        extrato = Extrato.objects.create(
            nome = nome,
            valor = valor,
            ganho_gasto = ganho_gasto,
            dono_id = id
        )

        extrato.save()
        data = {
            'status': 'extrato registrado'
        }
        return JsonResponse(data)

def pegar_extrato(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        id = listaDeValores[0]
        mes = datetime.date.today().month
        ano = datetime.date.today().year
        dia = '{}-{}'.format(ano, mes)
        data = []
        extratoFiltrado = Extrato.objects.filter(dono_id = id, dia__icontains = dia)
        for item in extratoFiltrado.all():
            data2 = {}
            data2['nome'] = item.nome
            data2['valor'] = item.valor
            data2['dia'] = item.dia
            data2['ganho_gasto'] = item.ganho_gasto
            data.append(data2)
        return JsonResponse(data, safe=False)

#fixos

def registrar_fixo(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        nome = listaDeValores[0]
        categoria = listaDeValores[1]
        valor = listaDeValores[2]
        pagamento = listaDeValores[3]
        banco = listaDeValores[4]
        dia_pagamento = listaDeValores[5]
        dono = listaDeValores[6]

        fixo = GastosFixos.objects.create(
            nome = nome,
            categoria = categoria,
            valor = valor,
            pagamento = pagamento,
            banco = banco,
            dia_pagamento = dia_pagamento,
            dono_id = dono,
        )

        fixo.save()

        data = {
            'status': 'fixo registrado'
        }
        return JsonResponse(data)
    
def pegar_fixo(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        id = listaDeValores[0]
        fixoFiltrado = GastosFixos.objects.filter(dono_id = id)
        data = []
        for item in fixoFiltrado.all():
            data2 = {}
            data2['nome'] = item.nome
            data2['categoria'] = item.categoria
            data2['valor'] = item.valor
            data2['pagamento'] = item.pagamento
            data2['banco'] = item.banco
            data2['dia_pagamento'] = item.dia_pagamento
            data2['id'] = item.pk
            data.append(data2)
        return JsonResponse(data, safe=False)

def deletar_fixo(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        id = listaDeValores[0]
        fixo = GastosFixos.objects.get(id = id)
        fixo.delete()
        data = {
            'status': 'deu tudo certo'
        }
        return JsonResponse(data)

def editar_fixo(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        nome = listaDeValores[0]
        categoria = listaDeValores[1]
        valor = listaDeValores[2]
        pagamento = listaDeValores[3]
        banco = listaDeValores[4]
        dia_pagamento = listaDeValores[5]
        id = listaDeValores[6]

        fixosdb = GastosFixos.objects.get(pk = id)
        fixosdb.nome = nome
        fixosdb.categoria = categoria
        fixosdb.valor = valor
        fixosdb.pagamento = pagamento
        fixosdb.banco = banco
        fixosdb.dia_pagamento = dia_pagamento

        fixosdb.save()

        data2 = {
            'status': 'fixo editado'
        }
    return JsonResponse(data2)

#temporarios 

def registrar_temporario(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        nome = listaDeValores[0]
        categoria = listaDeValores[1]
        valor = listaDeValores[2]
        pagamento = listaDeValores[3]
        banco = listaDeValores[4]
        dia_inicial = listaDeValores[5]
        dia_final = listaDeValores[6]
        dono = listaDeValores[7]

        temporario = GastosTemporarios.objects.create(
            nome = nome,
            categoria = categoria,
            valor = valor,
            pagamento = pagamento,
            banco = banco,
            dia_inicial = dia_inicial,
            dia_final = dia_final,
            dono_id = dono,
        )

        temporario.save()

        data = {
            'status': 'temporario registrado'
        }
        return JsonResponse(data)

def pegar_temporario(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        id = listaDeValores[0]
        temporarioFiltrado = GastosTemporarios.objects.filter(dono_id = id)
        data = []
        for item in temporarioFiltrado.all():
            data2 = {}
            data2['nome'] = item.nome
            data2['categoria'] = item.categoria
            data2['valor'] = item.valor
            data2['pagamento'] = item.pagamento
            data2['banco'] = item.banco
            data2['dia_inicial'] = item.dia_inicial
            data2['dia_final'] = item.dia_final
            data2['id'] = item.pk
            data.append(data2)
        return JsonResponse(data, safe=False)

def deletar_temporario(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        id = listaDeValores[0]
        temporario = GastosTemporarios.objects.get(id = id)
        temporario.delete()
        data = {
            'status': 'deu tudo certo'
        }
        return JsonResponse(data)

def editar_temporario(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        nome = listaDeValores[0]
        categoria = listaDeValores[1]
        valor = listaDeValores[2]
        pagamento = listaDeValores[3]
        banco = listaDeValores[4]
        dia_inicial = listaDeValores[5]
        dia_final = listaDeValores[6]
        id = listaDeValores[7]

        temporariodb = GastosTemporarios.objects.get(pk = id)
        temporariodb.nome = nome
        temporariodb.categoria = categoria
        temporariodb.valor = valor
        temporariodb.pagamento = pagamento
        temporariodb.banco = banco
        temporariodb.dia_inicial = dia_inicial
        temporariodb.dia_final = dia_final

        temporariodb.save()

        data2 = {
            'status': 'temporario editado'
        }
    return JsonResponse(data2)
