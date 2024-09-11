from django.contrib import admin
from .models import UserInfo

class UsuariosInfos(admin.ModelAdmin):
    list_display = ('pessoa', 'renda_mensal')
    list_display_links = ('pessoa', 'renda_mensal',)
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(UserInfo,UsuariosInfos)


