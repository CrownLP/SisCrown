# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_laptop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('serie', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('marca', models.CharField(choices=[('SAMSUNG', 'Samsung'), ('HP', 'Hp'), ('DELL', 'Dell'), ('ASUS', 'Asus'), ('ACER', 'Acer'), ('SONY', 'Sony'), ('COMPAQ', 'Compaq'), ('LENOVO', 'Lenovo'), ('AOC', 'AOC'), ('LG', 'Lg')], max_length=20)),
                ('modelo', models.CharField(max_length=30)),
                ('display', models.CharField(blank=True, choices=[('14', '14 Pulgadas'), ('15', '15 Pulgadas'), ('17', '17 Pulgadas'), ('19', '19 Pulgadas'), ('22', '22 Pulgadas'), ('24', '24 Pulgadas')], max_length=20)),
                ('departamento_adquisicion', models.CharField(blank=True, choices=[('LAPAZ', 'La Paz'), ('SANTACRUZ', 'Santa Cruz'), ('COCHABAMBA', 'Cochabamba'), ('ORURO', 'Oruro'), ('POTOSI', 'Potosi'), ('TARIJA', 'Tarija'), ('SUCRE', 'Sucre'), ('BENI', 'Beni'), ('PANDO', 'Pando')], max_length=20)),
                ('caracteristica', models.CharField(blank=True, max_length=50)),
                ('observacion', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='laptop',
            name='display',
            field=models.CharField(blank=True, choices=[('14', '14 Pulgadas'), ('15', '15 Pulgadas'), ('17', '17 Pulgadas'), ('19', '19 Pulgadas')], max_length=20),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='procesador',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='telefono_ip',
            name='marca',
            field=models.CharField(choices=[('ATCOM', 'Atcom'), ('GRANDSTREAM', 'GrandStream'), ('CISCO', 'Cisco'), ('AVAYA', 'Avaya'), ('POLYCOM', 'Polycom'), ('YEALINK', 'Yealink'), ('FANVIL', 'Fanvil')], max_length=20),
        ),
    ]
