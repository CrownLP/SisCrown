from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(max_length=500, blank=True)
    ubicacion = models.CharField(max_length=30, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

class Agencia (models.Model):
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
	departamento = models.CharField(max_length=20,blank=True, choices= DEPARTAMENTOS)
	observacion =  models.TextField(blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.numero
