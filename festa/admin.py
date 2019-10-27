from django.contrib import admin

from .models import *

from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"
pt_BR_formats.DATE_FORMAT = "d M Y"


class AluguelAdmin(admin.ModelAdmin):
    list_display = ('data', 'horainicio', 'horatermino', 'valor', 'tema_escolhido', 'local', 'cliente')
    date_hierarchy = ('data')
    search_fieldes = ('tema_escolhido',)
    list_filter = ['data', 'tema_escolhido']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fone')
    
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'bairro')

admin.site.register(ItemTema)
admin.site.register(Tema)    
admin.site.register(Aluguel, AluguelAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco, EnderecoAdmin)
    
# Register your models here.
