from django.db import models
from django.utils import timezone
from usuario.models import Agencia
from cliente.models import Cliente
from django.contrib.auth.models import User
# Create your models here.

class Visita (models.Model):
    # los campos de un Visita:
    # ID (generada automaticamente)
    # dni cliente
    # tipo de vehiculo
    # agencia
    # referencia
    # fecha de creacion
    # ejecutivo
    # vendedor

    id = models.AutoField(primary_key=True)
    dni = models.ForeignKey(Cliente, blank=False)#nombre de cliente
    TIPOVEHICULOS= (
    ('CAMION','Camion'),
    ('MOTO', 'Moto'),
    ('VEHICULOLIVIANO', 'Vehiculo Liviano')
    )
    tipo_vehiculos = models.CharField(max_length=30, choices= TIPOVEHICULOS, default='VEHICULOLIVIANO')
    REFERENCIAS= (
    ('PERSONAL','Personal'),
    ('REDES', 'Redes'),
    ('RADIO', 'Radio'),
    ('VOLANTES', 'Volantes'),
    ('SHOWROOM', 'Show Room'),
    ('OTRO', 'Otro')
    )
    referencia = models.CharField(max_length=30, choices= REFERENCIAS)
    vendedor = models.ForeignKey(User, blank = True, null = True)
    #campos que deben ser generados automaticamente
    agencia = models.ForeignKey(Agencia, blank=False)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    # def __str__(self):
    #     return self.id
