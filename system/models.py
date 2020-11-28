from django.db import models
from django.contrib.auth.models import User


STATUS = (
	(0, "Disponível"),
	(1, "Indisponível")

)

CATEGORIA = (
	(0, "Alto Padrão"),
	(1, "Médio Padrão"),
	(2, "Baixo Padrão")

)

NEGOCIO = (
	(0, "Aluguel"),
	(1, "Arrendamento"),
	(2, "Venda")

) 

class Imovel(models.Model):
	id = models.BigAutoField(primary_key=True)
	imagem = models.FileField (upload_to = 'media/', blank=True, null=True)	
	categoria = models.IntegerField(choices=CATEGORIA, default=0)
	negocio = models.IntegerField(choices=NEGOCIO, default=0)
	titulo = models.CharField(max_length=250, unique=True)
	endereco = models.CharField(max_length=300, unique=True)
	area = models.IntegerField(unique=True)
	num_quarto = models.IntegerField(unique=True)
	num_banheiro = models.IntegerField(unique=True)
	num_vaga = models.IntegerField(unique=True)
	descricao = models.TextField(unique=True)
	corretor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='system_imoveis')
	status = models.IntegerField(choices=STATUS, default=0)

	class Meta:
		verbose_name = "Imóvel"
		verbose_name_plural = "Imóveis"
		ordering = ['-titulo']

	def __str__(self):
		return self.titulo


class Galeria(models.Model):
	imovel = models.ForeignKey(Imovel, on_delete = models.CASCADE, related_name='Imagem_imoveis', null=True)
	imagem = models.ImageField("Imagem", upload_to='media/imoveis', blank=False, null=True)

	class Meta:
		verbose_name = "Galeria do Imóvel"
		verbose_name_plural = "Galeria do Imóvel"



class Corretor(models.Model):	
	nome = models.ForeignKey(User, on_delete=models.CASCADE, related_name='system_corretores')
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