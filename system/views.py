from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from . import forms, models
from django.http import HttpResponse
from .models import Corretor, Imovel
from django.views.generic import ListView
from .forms import CorretorForm, ImovelForm
from django.conf import settings



class CorretorList(ListView):
	model = Corretor


def lista_corretores(request):
	corretores = Corretor.objects.all()
	return render(request, 'lista_corretores.html',{"corretores":corretores})


def createCorretor(request):
    form = CorretorForm(request.POST)  
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/lista_corretores')
    return render(request, 'cadastrar_corretor.html',{'form':form} )


def visualizarCorretor(request, id):
    corretor = get_object_or_404(Corretor, pk=id)
    return render(request, 'visualizar_corretor.html', {'corretor': corretor})


def editarCorretor(request, id):
    corretor = get_object_or_404(Corretor, pk=id)
    form = CorretorForm(instance = corretor)
    if(request.method == 'POST'):
        form = CorretorForm(request.POST, instance=corretor)
        if(form.is_valid()):
            corretor.save()
            return redirect('/lista_corretores')
        else:
            return render(request, 'editar_corretor.html', {'form': form, 'corretor':corretor})
    else:
        return render(request, 'editar_corretor.html', {'form': form, 'corretor':corretor})        


def deleteCorretor(request, id):
    form = CorretorForm(request.POST)  
    corretor = Corretor.objects.get(id=id)  
    corretor.delete()  
    return redirect('/lista_corretores')
    return render(request, 'deletar_corretor.html',{'form':form})




class ImovelList(ListView):
    model = Imovel

def lista_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'lista_imoveis.html',{"imoveis":imoveis})


def createImovel(request):
    form = ImovelForm(request.POST)  
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/lista_imoveis')
    return render(request, 'cadastrar_imovel.html',{'form':form})


def visualizarImovel(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    return render(request, 'visualizar_imovel.html', {'imovel': imovel})


def editarImovel(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    form = ImovelForm(instance = imovel)
    if(request.method == 'POST'):
        form = ImovelForm(request.POST, instance=imovel)
        if(form.is_valid()):
            corretor.save()
            return redirect('/lista_imoveis')
        else:
            return render(request, 'editar_imovel.html', {'form': form, 'imovel':imovel})
    else:
        return render(request, 'editar_imovel.html', {'form': form, 'imovel':imovel})        


def deleteImovel(request, id):
    form = ImovelForm(request.POST)  
    imovel = Imovel.objects.get(id=id)  
    imovel.delete()  
    return redirect('/lista_imoveis')
    return render(request, 'deletar_imovel.html',{'form':form})



#Login#
def login_page(request):
    context = {
        'error_msg': ''
    }
    
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(settings.LOGIN_URL_REDIRECT)
        else:
            context = {
                'error_msg': 'Senha e/ou usuário inválido.'
            }
            return render(request, 'registration/login.html', context)

    return render(request, 'registration/login.html', context)

