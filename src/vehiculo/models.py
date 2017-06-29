from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Marca (models.Model):
	codigo = models.CharField(max_length=6,primary_key=True,blank = False,help_text="Inserte el Codigo de Marca",unique = True)
	nombre = models.CharField(max_length=50,blank=False,help_text="Inserte el Nombre de la Marca",unique = True)
	foto = models.ImageField (blank=False, help_text="Suba la foto de la Marca")
	garantia = models.IntegerField(null=True,blank = True, help_text="Garantia en Años")
	paginaweb = models.URLField(null=True, blank=True)
	descripcion = models.TextField (max_length= 100, blank = True)
	user = models.ForeignKey(User)
	observacion = models.TextField(blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.codigo
