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
	departamento_origen = models.CharField(max_length=20,blank=True, choices= DEPARTAMENTOS)
	caracteristica = models.CharField(max_length=50, blank=True)
	observacion =  models.TextField(blank=True)
	foto = models.ImageField (upload_to='foto_celular',blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.imei

class Telefono_IP (models.Model):
	#Numero de Serie
	serie = models.CharField(max_length=20,primary_key=True)
	MARCAS = (
	('ATCOM',''),
	('GRANDSTREAM','Samsung'),
	('CISCO', 'Nokia'),
	('AVAYA', 'Alcatel'),
	('POLYCOM','Polycom'),
	('YEALINK','Yealink'),
	('FANVIL','Fanvil')
	)
	marca = models.CharField(max_length=20,blank=False, choices= MARCAS)
	modelo = models.CharField(max_length=30, blank=False)
	mac = models.CharField(max_length=30,blank=True)
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
	departamento_adquisicion = models.CharField(max_length=20,blank=True, choices= DEPARTAMENTOS)
	caracteristica = models.CharField(max_length=50, blank=True)
	observacion =  models.TextField(blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.serie

class Linea_IP (models.Model):
	#Numero de Serie
	interno = models.CharField(max_length=20,primary_key=True)
	ip = models.CharField(max_length=30, blank=False)
	ip_central = models.CharField(max_length=30, blank=False)
	PERMISOS = (
	('CELULAR','Celular'),
	('LOCAL','Local'),
	('ESPECIAL', 'Especial'),
	)
	permisos = models.CharField(max_length=20,blank=True, choices= PERMISOS)
	observacion =  models.TextField(blank=True)
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
	departamento_creacion = models.CharField(max_length=20,blank=True, choices= DEPARTAMENTOS)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.interno

class Laptop (models.Model):
	#Numero de Serie
	serie = models.CharField(max_length=40,primary_key=True)
	MARCAS = (
	('HP','Hp'),
	('DELL','Dell'),
	('ASUS', 'Asus'),
	('ACER', 'Acer'),
	('SAMSUNG','Samsung'),
	('TOSHIBA','Toshiba'),
	('COMPAQ','Compaq'),
	('LENOVO','Lenovo'),
	('MAC','Mac'),
	)
	marca = models.CharField(max_length=20,blank=False, choices= MARCAS)
	modelo = models.CharField(max_length=30, blank=False)
	SO = (
	('WIN10','Windows 10'),
	('WIN8','Windows 8'),
	('WIN7', 'Windows 7'),
	('WINXP', 'Windows XP'),
	('MACOS', 'macOS'),
	('UBUNTU', 'Ubuntu'),
	('DEBIAN', 'Debian'),
	('REDHAT', 'Red Hat'),
	('MINT', 'Mint'),
	)
	procesador = models.CharField(max_length=20,blank=True, choices= SO)
	#cambiar a radio buton
	arquitectura = models.CharField(max_length=40)
 	RAM = (
	('2','2 Gb'),
	('4', '4 Gb'),
	('8', '8 Gb'),
	('12', '12 Gb'),
	('16', '16 Gb'),
	('32', '32 Gb')
	)
	ram = models.CharField(max_length=20,blank=True, choices= RAM)
	RAM = (
	('250','250 Gb'),
	('500', '500 Gb'),
	('750', '750 Gb'),
	('1024', '1 Tb')
	)
	ram = models.CharField(max_length=20,blank=True, choices= RAM)


	observacion =  models.TextField(blank=True)
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
	departamento_creacion = models.CharField(max_length=20,blank=True, choices= DEPARTAMENTOS)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.interno
