from django.db import models

# Create your models here.

class Pozos(models.Model):

    # Nivel de fluoruro
    # OMS/WHO Limite = 1.5 mg/L
    fluoruro = models.FloatField()

	# Nivel de Arsenico
    # OMS/WHO Limite = 10 ug/L
    arsenico = models.IntegerField()

    # siempre fecha de hoy para evitar errores
    fecha = models.DateField(auto_now=True)
