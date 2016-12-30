# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text=b'Titulo de Categoria', max_length=100)),
                ('slug', models.SlugField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinkMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('icono', models.CharField(blank=True, max_length=100)),
                ('link', models.CharField(blank=True, max_length=100)),
                ('estilo', models.CharField(blank=True, max_length=100)),
                ('orden', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100)),
                ('estilo', models.CharField(blank=True, max_length=100)),
                ('template', models.CharField(blank=True, max_length=100)),
                ('seccion', models.CharField(blank=True, help_text=b'El id donde se colocara', max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('paginas', models.ManyToManyField(blank=True, related_name='menus', to='cmsweb.Pagina')),
            ],
        ),
        migrations.AddField(
            model_name='linkmenu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='cmsweb.Menu'),
        ),
        migrations.AddField(
            model_name='pagina',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmsweb.Categoria'),
        ),
    ]