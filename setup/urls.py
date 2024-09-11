from django.contrib import admin
from django.urls import path,include
from api_ganhos_gastos.views import ExtratoViewSet, deletar_fixo, deletar_temporario, editar_fixo, editar_temporario, pegar_fixo, pegar_temporario, registrar_fixo,registrar_gastos,editar_gastos, registrar_ganhos, editar_ganhos, Registrar_extrato, pegar_extrato, registrar_temporario
from api_user.views import UserViewSet, UserInfoViewSet, login_api, Pegar_renda, registrar_api, deletar_usuario,registrar_renda
from rest_framework import routers


router = routers.DefaultRouter()
router.register('extrato', ExtratoViewSet, basename='Extrato')
router.register('users', UserViewSet, basename='Users')
router.register('usersinfo', UserInfoViewSet, basename='UsersInfo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('login/',login_api, name='login'),
    path('registrar/',registrar_api, name='registrar'),
    path('registrar_renda/',registrar_renda, name='registrarR'),
    path('registrar_gasto/',registrar_gastos, name='registrarG'),
    path('editar_gasto/',editar_gastos, name='editarG'),
    path('registrar_ganho/',registrar_ganhos, name='registrarGa'),
    path('editar_ganho/',editar_ganhos, name='editarGa'),
    path('registrar_extrato/',Registrar_extrato, name='registrarE'),
    path('pegar_extrato/',pegar_extrato, name='pegarE'),
    path('registrar_fixo/',registrar_fixo, name='registrarF'),
    path('pegar_fixo/',pegar_fixo, name='pegarF'),
    path('editar_fixo/',editar_fixo, name='editarF'),
    path('deletar_fixo/',deletar_fixo, name='deletarF'),
    path('registrar_temporario/',registrar_temporario, name='registrarT'),
    path('pegar_temporario/',pegar_temporario, name='pegarT'),
    path('editar_temporario/',editar_temporario, name='editarT'),
    path('deletar_temporario/',deletar_temporario, name='deletarT'),
    path('deletar/',deletar_usuario, name='deletar'),
    path('renda/',Pegar_renda, name='renda'),
]
