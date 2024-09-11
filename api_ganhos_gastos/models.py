from django.db import models
from datetime import date
from django.contrib.auth.models import User

OPCOES_CATEGORIA = [
    ('Lazer','Lazer'),
    ('Comida','Comida'),
    ('Tecnologia','Tecnologia'),
    ('viagem','viagem'),
    ('outros','outros'),
]

OPCOES_PAGAMENTO = [
    ('Dinheiro','Dinheiro'),
    ('Cartão de crédito','Cartão de crédito'),
    ('Cartão de débito','Cartão de débito'),
    ('Cheque','Cheque'),
    ('Pix','Pix'),
    ('Outros','Outros'),
]

OPCOES_CATEGORIA_GANHOS =[
    ('Trabalho','Trabalho'),
    ('Freelancer','Freelancer'),
    ('Presente','Presente'),
    ('Outros','Outros'),
]

class Gastos(models.Model):
    nome = models.CharField( null=False, blank=False, max_length=100)
    categoria = models.CharField(null=False, blank=False,choices=OPCOES_CATEGORIA, max_length=100)
    valor = models.CharField(null=False, blank=False, max_length=100)
    pagamento = models.CharField(null=False, blank=False,choices=OPCOES_PAGAMENTO, max_length=100)
    banco = models.CharField(null=False,blank=False, max_length=100)
    dia = models.DateField(default=date.today, blank=False)
    dono = models.ForeignKey(to= User, on_delete=models.CASCADE, null=False, blank=False, related_name="dono")

class Ganhos(models.Model):
    nome = models.CharField( null=False, blank=False, max_length=100)
    categoria = models.CharField(null=False, blank=False,choices=OPCOES_CATEGORIA_GANHOS, max_length=100)
    valor = models.CharField(null=False, blank=False, max_length=100)
    banco = models.CharField(null=False,blank=False, max_length=100)
    dia = models.DateField(default=date.today, blank=False)
    dono = models.ForeignKey(to= User, on_delete=models.CASCADE, null=False, blank=False, related_name="dono2")

class Extrato(models.Model):
    nome = models.CharField( null=False, blank=False, max_length=100)
    valor = models.CharField(null=False, blank=False, max_length=100)
    dia = models.DateField(default=date.today, blank=False)
    ganho_gasto = models.IntegerField(null=False, blank=False,)
    dono = models.ForeignKey(to= User, on_delete=models.CASCADE, null=False, blank=False, related_name="dono3")

class GastosFixos(models.Model):
    nome = models.CharField( null=False, blank=False, max_length=100)
    categoria = models.CharField(null=False, blank=False,choices=OPCOES_CATEGORIA, max_length=100)
    valor = models.CharField(null=False, blank=False, max_length=100)
    pagamento = models.CharField(null=False, blank=False,choices=OPCOES_PAGAMENTO, max_length=100)
    banco = models.CharField(null=False,blank=False, max_length=100)
    dia_pagamento = models.CharField(null=False,blank=False, max_length=100)
    dono = models.ForeignKey(to= User, on_delete=models.CASCADE, null=False, blank=False, related_name="dono4")

class GastosTemporarios(models.Model):
    nome = models.CharField( null=False, blank=False, max_length=100)
    categoria = models.CharField(null=False, blank=False,choices=OPCOES_CATEGORIA, max_length=100)
    valor = models.CharField(null=False, blank=False, max_length=100)
    pagamento = models.CharField(null=False, blank=False,choices=OPCOES_PAGAMENTO, max_length=100)
    banco = models.CharField(null=False,blank=False, max_length=100)
    dia_inicial = models.CharField(null=False,blank=False, max_length=100)
    dia_final = models.CharField(null=False,blank=False, max_length=100)
    dono = models.ForeignKey(to= User, on_delete=models.CASCADE, null=False, blank=False, related_name="dono5")
