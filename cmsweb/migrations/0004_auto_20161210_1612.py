# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-10 16:12
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsweb', '0003_auto_20161210_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloque',
            name='contenido',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='pagina',
            name='contenido',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]