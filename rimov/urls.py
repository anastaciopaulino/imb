from django.views.generic import TemplateView, RedirectView
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from system import views


urlpatterns = [

	path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')),
	
	path('', TemplateView.as_view(template_name="index.html")),
	path('painel/', TemplateView.as_view(template_name="painel.html")),
	
	
	
	path('painel/imoveis/', TemplateView.as_view(template_name="imoveis.html")),	
	path('painel/google_maps/', TemplateView.as_view(template_name="google_maps.html")),
	

    
	path('painel/lista_corretores/', views.lista_corretores, name='lista_corretores'),
	path('painel/criar_corretor/', views.createCorretor, name="criar_corretor"),
	path('visualizar_corretor/<str:id>', views.visualizarCorretor, name="visualizar_corretor"),
	path('editar_corretor/<str:id>', views.editarCorretor, name='editar_corretor'),	
	path('deletar_corretor/<str:id>/', views.deleteCorretor),



	path('painel/lista_imoveis/', views.lista_imoveis, name='lista_imoveis'),
	path('painel/criar_imovel/', views.createImovel, name="criar_imovel"),
	path('visualizar_imovel/<str:id>', views.visualizarImovel, name="visualizar_imovel"),
	path('editar_imovel/<str:id>', views.editarImovel, name="editar_imovel"),	
	path('deletar_imovel/<str:id>/', views.deleteImovel),
    
       
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

