from django.contrib import admin
from .models import Imovel, Corretor, Galeria


class ImoGal(admin.TabularInline):
	model = Galeria
	extra = 0

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulo', 'propriedade', 'negocio', 'categoria', 'imagem', 
					'localizacao', 'endereco', 'area', 'num_quarto', 'num_banheiro',
					'num_vaga', 'descricao', 'corretor', 'status')
	list_filter = ('status',)
	search_fields = ['titulo', 'corretor']
	inlines=[ImoGal]




class GaleriaAdmin(admin.ModelAdmin):
	list_display = ('imovel', 'imagem')
	list_filter = ('imovel',)
	search_fields = ['imovel']



class CorretorAdmin(admin.ModelAdmin):
	list_display = ('nome','numero_cri','telefone','endereco', 'email')
	list_filter = ('nome',)
	search_fields = ['nome', 'email']


admin.site.register(Corretor, CorretorAdmin)


# Register your models here.
