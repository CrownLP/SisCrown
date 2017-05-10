from django.db import models
from django.utils import timezone


# Create your models here.
class Marca (models.Model):
	codigo = models.CharField(max_length=20,primary_key=True)
    nombre = model.CharField(max_length=20, blank = False)
    descripcion =  models.TextField(blank=True)
    observacion =  models.TextField(blank=True)
	PAISES = (
	('TIGO','Tigo'),
	('ENTEL', 'Entel'),
	('VIVA', 'Viva')
	)
	pais = models.CharField(max_length=20,blank=True, choices= PAISES)
    fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.marca
