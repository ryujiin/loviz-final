# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=b'material/imagen/')),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlantaPVC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utiles.Color')),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utiles.Talla')),
            ],
        ),
        migrations.CreateModel(
            name='PrecioMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(blank=True, decimal_places=2, help_text=b'Este es el precio del material', max_digits=10, null=True)),
                ('unidad_medida', models.CharField(blank=True, choices=[(b'metros', b'Metros'), (b'centimetros', b'Centimetros'), (b'unidades', b'Unidades'), (b'docenas', b'Docenas'), (b'paquetes', b'paquetes'), (b'kilos', b'Kilos')], max_length=100, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
                ('material', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='material.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('ruc', models.CharField(blank=True, max_length=11)),
                ('telefono', models.CharField(blank=True, max_length=11)),
                ('direccion', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(blank=True, choices=[(b'mas', b'Aumenta'), (b'menos', b'Disminuye')], max_length=100, null=True)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, help_text=b'Este es la cantidad que se modifica en el stock', max_digits=10, null=True)),
                ('stock', models.DecimalField(blank=True, decimal_places=2, help_text=b'Este es el stock que hay de este material', max_digits=10, null=True)),
                ('material', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='material.Material')),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='proveedor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='material.Proveedor'),
        ),
        migrations.AddField(
            model_name='material',
            name='tipo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='material.MaterialTipo'),
        ),
    ]
