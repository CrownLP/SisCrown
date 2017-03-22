from django.db import models
from django.utils import timezone

# Create your models here.
class Instancia (models.Model):
	numero = models.CharField(max_length=20,primary_key=True)
	sim = models.CharField(max_length=20)
	OPERADORES= (
	('TIGO','Tigo'),
	('ENTEL', 'Entel'),
	('VIVA', 'Viva')
	)
	operador = models.CharField(max_length=20,blank=True, choices= OPERADORES)
	plan = models.CharField(max_length=50, blank=True)
	DEPARTAMENTOS = (
	('LAPAZ','La Paz'),
	('SANTACRUZ','Santa Cruz'),
	('COCHABAMBA', 'Cochabamba'),
	('ORURO', 'Oruro'),
	('POTOSI', 'Potosi'),
	('TARIJA', 'Tarija'),
	('SUCRE', 'Sucre'),
	('BENI', 'Beni'),
	('PANDO', 'Pando')
	)
	departamento_origen = models.CharField(max_length=20,blank=True, choices= DEPARTAMENTOS)
	observacion =  models.TextField(blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.numero

class Celular (models.Model):
	#Datos del Equipo
	imei = models.CharField(max_length=20,primary_key=True)
	#la instancia debe recibir una relacion 1:1
	instancia = models.OneToOneField(Instancia, null = True, blank = True)
	#instancia = models.CharField()
	#asignacion a un usuario
	MARCAS = (
	('null',''),
	('SAMSUNG','Samsung'),
	('NOKIA', 'Nokia'),
	('ALCATEL', 'Alcatel'),
	('HUAWEI', 'Huawei'),
	('SONY', 'Sony'),
	('APPLE', 'Apple')
	)
	marca = models.CharField(max_length=20,blank=True, choices= MARCAS)
	modelo = models.CharField(max_length=30, blank=False)
	DEPARTAMENTOS = (
	('LAPAZ','La Paz'),
	('SANTACRUZ','Santa Cruz'),
	('COCHABAMBA', 'Cochabamba'),
	('ORURO', 'Oruro'),
	('POTOSI', 'Potosi'),
	('TARIJA', 'Tarija'),
	('SUCRE', 'Sucre'),
	('BENI', 'Beni'),
	('PANDO', 'Pando')
	)
	departamento_origenSSSS = models.CharField(max_length=20,blank=True, choices= DEPARTAMENTOS)
	caracteristica = models.CharField(max_length=50, blank=True)
	observacion =  models.TextField(blank=True)
	foto = models.ImageField (upload_to='foto_celular',blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.imei
