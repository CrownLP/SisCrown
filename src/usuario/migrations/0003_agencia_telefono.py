# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-10 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20170703_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencia',
            name='telefono',
            field=models.IntegerField(blank=True, help_text='Telefono de Contacto', null=True),
        ),
    ]