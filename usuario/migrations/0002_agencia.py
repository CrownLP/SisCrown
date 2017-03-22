# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('numero', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sim', models.CharField(max_length=20)),
                ('operador', models.CharField(blank=True, choices=[('TIGO', 'Tigo'), ('ENTEL', 'Entel'), ('VIVA', 'Viva')], max_length=20)),
                ('plan', models.CharField(blank=True, max_length=50)),
                ('departamento', models.CharField(blank=True, choices=[('LAPAZ', 'La Paz'), ('SANTACRUZ', 'Santa Cruz'), ('COCHABAMBA', 'Cochabamba'), ('ORURO', 'Oruro'), ('POTOSI', 'Potosi'), ('TARIJA', 'Tarija'), ('SUCRE', 'Sucre'), ('BENI', 'Beni'), ('PANDO', 'Pando')], max_length=20)),
                ('observacion', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
