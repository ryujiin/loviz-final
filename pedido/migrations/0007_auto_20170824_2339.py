# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-24 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0006_metodoenvio_icono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metodoenvio',
            name='icono',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
