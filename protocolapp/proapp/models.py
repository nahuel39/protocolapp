from django.db import models

# Create your models here.
class Visitas (models.Model): 
    celular = models.IntegerField()
    fecha = models.DateTimeField(auto_now=True)

