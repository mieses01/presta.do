# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_do', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='id_cli',
            field=models.ForeignKey(default=0, to='presta_do.Cliente'),
            preserve_default=False,
        ),
    ]
