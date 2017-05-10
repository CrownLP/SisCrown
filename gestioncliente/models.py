from django.db import models
from django.utils import timezone
# Create your models here.

class Visita (models.Model):
    ficha2 = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)
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
    sucursal =  models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    def __str__(self):
	       return self.ficha2
    #modulo de registro de visita de cliente a show room
    #el numero de ficha estara compuesto por:
    #departamento
    #fecha
    #autoincremental
