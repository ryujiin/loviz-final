# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-25 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0008_auto_20170825_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metodopago',
            name='iconos',
        ),
        migrations.AddField(
            model_name='metodopago',
            name='img',
            field=models.ImageField(blank=True, upload_to=b'tienda'),
        ),
    ]
