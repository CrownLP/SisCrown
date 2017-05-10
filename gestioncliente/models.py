from django.db import models
from django.utils import timezone
# Create your models here.

class Visita (models.Model):
    
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
