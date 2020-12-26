from django.forms import ModelForm
from .models import Corretor
from .models import Imovel
from django import forms

class CorretorForm(ModelForm):
	class Meta:
		model = Corretor
		fields = '__all__'


class ImovelForm(ModelForm):
	class Meta:
		model = Imovel
		fields = '__all__'
		
     
class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))