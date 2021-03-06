# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-09 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsweb', '0004_auto_20161210_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text=b'El titulo para identificar el hero', max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(upload_to=b'hero')),
                ('body', models.CharField(blank=True, help_text=b'El texto que se mostrara', max_length=100)),
                ('estilo_body', models.CharField(blank=True, help_text=b'Los estilos del texto que se mostrara', max_length=100)),
            ],
        ),
    ]
