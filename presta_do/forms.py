from django.forms import  ModelForm
from django import  forms
from presta_do.models import Cliente,Ingreso,Referencia,Otros

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente