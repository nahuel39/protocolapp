from django.db import models

# Create your models here.
class Visitas (models.Model): 
    celular = models.IntegerField()
    fecha = models.DateTimeField(auto_now=True)
    #local = models.ForeignKey(Negocio, on_delete = models.CASCADE)



class Negocio(models.Model):
    usuario    = models.CharField(max_length = 30)
    nombre     = models.CharField(max_length = 30)
	#direccion  = models.CharField(max_length = 50)
    horario =  models.CharField(max_length = 4)
	#telefono   = models.IntegerField(null=True,blank=True)
    responsable = models.CharField(max_length = 30)