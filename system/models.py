from django.db import models
from django.contrib.auth.models import User


STATUS = (
	(0, "Disponível"),
	(1, "Indisponível")

)
TIPO_PROPRIEDADE =(
	(0, "Apartamento"),
	(1, "Casa"),
	(2, "Casa Condomínio"),
	(3, "Casa Vila"),
	(4, "Cobertura"),
	(5, "Comercial"),
	(6, "Fazenda"),
	(7, "Flat"),
	(8, "Kitnet"),
	(9, "Loft"),
	(10, "Sobrado"),
	(11, "Terreno Padrão"),

)

CATEGORIA = (
	(0, "Alto Padrão"),
	(1, "Médio Padrão"),
	(2, "Baixo Padrão")

)

NEGOCIO = (
	(0, "Aluguel"),
	(1, "Arrendamento"),
	(2, "Em Construção"),
	(3, "Venda")

) 

class Imovel(models.Model):
	id = models.BigAutoField(primary_key=True)
	titulo = models.CharField(max_length=250, unique=True)
	propriedade = models.TextField(choices=TIPO_PROPRIEDADE, default=0)
	negocio = models.TextField(choices=NEGOCIO, default=0)
	categoria = models.TextField(choices=CATEGORIA, default=0)
	imagem = models.FileField (upload_to = 'media/', blank=True, null=True)	
	localizacao = models.CharField(max_length=300, unique=True)
	endereco = models.CharField(max_length=300, unique=True)
	area = models.IntegerField(unique=True)
	num_quarto = models.IntegerField(unique=True)
	num_banheiro = models.IntegerField(unique=True)
	num_vaga = models.IntegerField(unique=True)
	descricao = models.TextField(unique=True)
	corretor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='system_imoveis')
	status = models.TextField(choices=STATUS, default=0)

	class Meta:
		verbose_name = "Imóvel"
		verbose_name_plural = "Imóveis"
		ordering = ['-pk']

	def __str__(self):
		return self.titulo


class Galeria(models.Model):
	imovel = models.ForeignKey(Imovel, on_delete = models.CASCADE, related_name='Imagem_imoveis', null=True)
	imagem = models.ImageField("Imagem", upload_to='media/imoveis', blank=False, null=True)

	class Meta:
		verbose_name = "Galeria do Imóvel"
		verbose_name_plural = "Galeria do Imóvel"



class Corretor(models.Model):
	id = models.BigAutoField(primary_key=True)	
	nome = models.ForeignKey(User, on_delete=models.CASCADE, related_name='system_corretores')
	foto = models.FileField (upload_to = 'media/', blank=True, null=True)
	numero_cri = models.IntegerField(default=0)
	telefone = models.CharField(max_length=250, unique=True)
	endereco = models.CharField(max_length=300, unique=True)
	email = models.EmailField(unique=True)
	

	class Meta:
		verbose_name = "Corretor"
		verbose_name_plural = "Corretores"
		ordering = ['-pk']

	def __str__(self):
		return self.email