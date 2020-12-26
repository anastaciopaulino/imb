from django.urls import path
from . import views
from system import views

urlpatterns = [	

	path('login/', views.login_page, name='login'),
	

	path('lista_corretores/', views.lista_corretores, name='lista_corretores'),
	path('criar_corretor/', views.createCorretor, name="criar_corretor"),
	path('visualizar_corretor/<str:id>', views.visualizarCorretor, name="visualizar_corretor"),
	path('editar_corretor/<str:id>', views.editarCorretor, name="editar_corretor"),
	
	path('deletar_corretor/<str:id>/', views.deleteCorretor),


	path('lista_imoveis/', views.lista_imoveis, name='lista_imoveis'),
	path('criar_imovel/', views.createImovel, name="criar_imovel"),
	path('visualizar_imovel/<str:id>', views.visualizarImovel, name="visualizar_imovel"),
	path('editar_imovel/<str:id>', views.editarImovel, name="editar_imovel"),
	
	path('deletar_imovel/<str:id>/', views.deleteImovel),    
]

