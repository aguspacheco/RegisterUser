from django.db import models
from django.contrib.auth.models import User

class Formulario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    ejido = models.ForeignKey('Ejido', on_delete=models.CASCADE)
    chacra = models.IntegerField(null=True, blank=True)
    fraccion = models.IntegerField(null=True, blank=True)
    quinta = models.IntegerField(null=True, blank=True)
    lote = models.IntegerField(null=True, blank=True)
    macizo = models.IntegerField(null=True, blank=True)
    manzana = models.IntegerField(null=True, blank=True)
    unidad_funcional = models.IntegerField(null=True, blank=True)

class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ejido(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.departamento) + ' - ' + self.nombre