import io
from .models import UserInfo
from django.contrib.auth.models import User
from .serializers import UserSerializer,UserInfoSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib import auth
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from rest_framework.authtoken.models import Token


for user in User.objects.all():
    if Token.objects.filter(user=user).exists()== False:
        print(user)
        Token.objects.get_or_create(user=user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserInfoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

def login_api(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)

        nome = listaDeValores[0]
        senha = listaDeValores[1]
        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )
        data = {}
        if usuario is not None:
            auth.login(request, usuario)
            print(request.user)
            print(Token.objects.get(user_id=request.user))
            data['id'] = usuario.pk
            data['username'] = usuario.username
            data['email'] = usuario.email
            data['token'] = str(Token.objects.get(user_id=request.user))
            print(data)
        
    return JsonResponse(data)

def Pegar_renda(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        idrenda = listaDeValores[0]
        data = {}
        if UserInfo.objects.filter(pessoa_id=idrenda).exists():
            renda = float(UserInfo.objects.get(pessoa_id=idrenda).renda_mensal)
            data['renda_mensal'] = renda
        else:
            data['renda_mensal'] = -1.0

        return JsonResponse(data)

def registrar_api(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        username = listaDeValores[0]
        email = listaDeValores[1]
        password = listaDeValores[2]

        usuario = User.objects.create_user(
            username = username,
            email= email,
            password= password
        )
        usuario.save()
        data = {
            'status': 'deu tudo certo'
        }
        usertoken = User.objects.get(username=username)
        Token.objects.get_or_create(user=usertoken)
        return JsonResponse(data)
    
def registrar_renda(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        renda_mensal = listaDeValores[0]
        user_id = listaDeValores[1]
        renda = UserInfo.objects.create(
            renda_mensal = renda_mensal,
            pessoa_id = user_id,
        )
        renda.save()
        data = {
            'status': 'renda registrada'
        }
        return JsonResponse(data)

def deletar_usuario(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        listaDeValores = []
        for v in data.values():
            listaDeValores.append(v)
        user_id = listaDeValores[0]
        perfilD = User.objects.get(id = user_id)
        perfilD.delete()
        data = {
            'status': 'deu tudo certo'
        }
        return JsonResponse(data)