from django.db import models

SEX_CHOICES = (
    ("1", "Masculino"),
    ("2", "Femenino"),
)
DOCUM_CHOICES = (
    ("CED", "Cedula"),
    ("PAS", "Pasaporte"),
)

class Cliente(models.Model):
    tipdocum = models.CharField(max_length=3,choices=DOCUM_CHOICES,default="CED")
    iddocum = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    alias = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=200)
    est_civil = models.CharField(max_length=1)
    sexo = models.CharField(max_length=1,choices=SEX_CHOICES,default=1)
    direccion1 = models.CharField(max_length=300)
    direccion2 = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__(self):
        return self.nombre

class Ingreso(models.Model):
    id_cli = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    superior = models.CharField(max_length=300)
    cargo = models.CharField(max_length=200)
    ingreso = models.DecimalField(max_digits=5, decimal_places=2)
    frecuencia = models.CharField(max_length=1)
    tipo = models.CharField(max_length=1)
    contacto = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    ext = models.CharField(max_length=5)
    correo = models.EmailField()

    def __unicode__(self):
        return self.nombre

class Referencia(models.Model):
    id_cli = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=300)
    asunto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1)

    def __unicode__(self):
        return self.nombre

class Otros(models.Model):
    id_cli = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=15)
    ext = models.CharField(max_length=5)
    celular = models.CharField(max_length=15)
    tipo = models.CharField(max_length=1)

    def __unicode__(self):
        return self.nombre

class sexo(models.Model):
    sexo = models.CharField(max_length=20)
    def __unicode__(self):
        return  self.sexo