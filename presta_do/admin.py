from django.contrib import admin
from .models import Cliente,Referencia,Ingreso,Otros
admin.site.register(Cliente)
admin.site.register(Referencia)
admin.site.register(Ingreso)
admin.site.register(Otros)
