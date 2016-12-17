# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_do', '0003_otros_referencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='sexo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(default=1, max_length=1, choices=[(b'1', b'Masculino'), (b'2', b'Femenino')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipdocum',
            field=models.CharField(default=b'CED', max_length=3, choices=[(b'CED', b'Cedula'), (b'PAS', b'Pasaporte')]),
        ),
    ]
