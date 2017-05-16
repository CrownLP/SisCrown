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
    #los campos de una agencia:
    #codigo
    #NOMBRE
    #foto
    #descripcion
    #empresa
    #pais
    #ciudad
    #direccion
    #ubicacion googlemaps
    #telefono
    ##responsable##
    #observacion
    #fecha_creacion
    codigo = models.CharField(max_length=20,primary_key=True,blank = False,help_text="Codigo de la Agencia",unique = True)
    nombre = models.CharField(max_length=50,blank=False,help_text="Nombre de la Agencia",unique = True)
    foto = models.ImageField (upload_to='foto_agencia',blank=True, help_text="Suba la foto de la Sucursal")
    descripcion = models.CharField (max_length= 100, blank = True)
    EMPRESAS= (
    ('CROWN','Crown'),
    ('TOYOSA', 'Toyosa'),
    ('TOYOTA', 'Toyota')
    )
    empresa = models.CharField(max_length=30,blank=False, choices= EMPRESAS)
    PAISES= (
    ('BOLIVIA','Bolivia'),
    ('CHILE', 'Chile'),
    ('CUBA', 'Cuba'),
    ('EEUU', 'Estados Unidos')
    )
    pais = models.CharField(max_length=30,blank=False, choices= PAISES)
    CIUDADES= (
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
    ciudad = models.CharField(max_length=20,blank=False, choices= CIUDADES)
    referencia = models.CharField (max_length= 150, blank = True)
    lat = models.CharField(max_length = 50)
    lng = models.CharField(max_length = 50)
    user = models.ForeignKey(User)
    observacion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.nombre
