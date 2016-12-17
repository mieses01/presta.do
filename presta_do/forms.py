from django.forms import  ModelForm,Textarea
from django import  forms
from presta_do.models import Cliente,Ingreso,Referencia,Otros

class ClienteForm(ModelForm):

    
    class Meta:
        model = Cliente
        fields = ('tipdocum','iddocum','nombre','apellido','alias','ocupacion','est_civil','sexo','direccion1','direccion2','pais','ciudad','email',)


