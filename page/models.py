from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ejido(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    codigo_dpto = models.IntegerField()

    def __str__(self):
        return self.codigo_dpto + '- by' + self.nombre
