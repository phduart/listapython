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
                ('cpf_cnpj', models.CharField(max_length=16)),
                ('nm_costume', models.CharField(max_length=255)),
                ('is_active', models.CharField(max_length=1)),
                ('vl_total', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
