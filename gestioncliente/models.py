from django.db import models
from django.utils import timezone
from usuario.models import Agencia
from cliente.models import Cliente
from django.contrib.auth.models import User
# Create your models here.

class Visita (models.Model):

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

class Oportunidad (models.Model):

    id = models.AutoField(primary_key=True)
    negociacion =  models.TextField(blank=False)
    dni = models.ForeignKey(Cliente, blank=False)#nombre de cliente
    modelo_actual = models.CharField(max_length=50, blank=True)
    modelo_interes = models.CharField(max_length=50, blank=True)
    VENTA= (
    ('CONTADO','Contado'),
    ('CREDITO', 'Credito'),
    ('AUTOFACIL', 'AutoFacil'),
    ('OTRO', 'Otro'),
    )
    tipo_venta = models.CharField(max_length=30, choices= VENTA, default='OTRO')
    ESTADOS= (
    ('VIGENTE','Vigente'),
    ('EXITOSA', 'Venta Exitosa'),
    ('CAIDA', 'Venta Caida'),
    ('SUSPENDIDA', 'Suspendida Temporalmente'),
    )
    estado = models.CharField(max_length=30, choices= ESTADOS, default='VIGENTE')
    vendedor = models.ForeignKey(User, blank = True)
    agencia = models.ForeignKey(Agencia, blank=False)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    # def __str__(self):
    #     return self.id
