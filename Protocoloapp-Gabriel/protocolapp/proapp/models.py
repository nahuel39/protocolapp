from django.db import models

# Create your models here.
class Negocio(models.Model):
	id_negocio = models.AutoField(primary_key=True)
	# password = models.CharField(max_length=50)
	direccion = models.CharField(max_length=25)
	nombre_local= models.CharField(max_length=20)
	nom_responsable = models.CharField(max_length=20)


class Visitas (models.Model): 
    celular = models.IntegerField(max_length=15)

class Positivo(models.Model):
	fecha_test=models.DateTimeField(auto_now=True)
	celular = models.ForeignKey(Visitas, on_delete=models.PROTECT)
