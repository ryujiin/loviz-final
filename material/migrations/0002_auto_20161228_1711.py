# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-28 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantapvc',
            name='color',
        ),
        migrations.RemoveField(
            model_name='plantapvc',
            name='talla',
        ),
        migrations.DeleteModel(
            name='PlantaPVC',
        ),
    ]