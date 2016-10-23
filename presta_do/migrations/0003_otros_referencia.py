# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_do', '0002_ingreso_id_cli'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=300)),
                ('telefono', models.CharField(max_length=15)),
                ('ext', models.CharField(max_length=5)),
                ('celular', models.CharField(max_length=15)),
                ('tipo', models.CharField(max_length=1)),
                ('id_cli', models.ForeignKey(to='presta_do.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=300)),
                ('asunto', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=1)),
                ('id_cli', models.ForeignKey(to='presta_do.Cliente')),
            ],
        ),
    ]
