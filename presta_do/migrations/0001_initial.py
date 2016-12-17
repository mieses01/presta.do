# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipdocum', models.CharField(max_length=3)),
                ('iddocum', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('alias', models.CharField(max_length=100)),
                ('ocupacion', models.CharField(max_length=200)),
                ('est_civil', models.CharField(max_length=1)),
                ('sexo', models.CharField(max_length=1)),
                ('direccion1', models.CharField(max_length=300)),
                ('direccion2', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=300)),
                ('superior', models.CharField(max_length=300)),
                ('cargo', models.CharField(max_length=200)),
                ('ingreso', models.DecimalField(max_digits=5, decimal_places=2)),
                ('frecuencia', models.CharField(max_length=1)),
                ('tipo', models.CharField(max_length=1)),
                ('contacto', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('ext', models.CharField(max_length=5)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
    ]
