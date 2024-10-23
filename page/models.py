from django.db import models
from django.contrib.auth.models import User

class Formulario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    ejidoAnterior = models.ForeignKey('Ejido', on_delete=models.CASCADE, related_name='formularios_anteriores')
    chacraAnterior = models.IntegerField(null=True, blank=True)
    fraccionAnterior = models.IntegerField(null=True, blank=True)
    quinta = models.IntegerField(null=True, blank=True)
    lote = models.IntegerField(null=True, blank=True)
    macizoAnterior = models.IntegerField(null=True, blank=True)
    manzanaAnterior = models.IntegerField(null=True, blank=True)
    unidad_funcionalAnterior = models.IntegerField(null=True, blank=True)

    ejidoActual = models.ForeignKey('Ejido', on_delete=models.CASCADE, related_name='formularios_actuales')
    circunscripcion = models.IntegerField(null=True, blank=True)
    sector = models.IntegerField(null=True, blank=True)
    chacraActual = models.IntegerField(null=True, blank=True)
    fraccionActual = models.IntegerField(null=True, blank=True)
    macizoActual = models.IntegerField(null=True, blank=True)
    manzanaActual = models.IntegerField(null=True, blank=True)
    parcela = models.IntegerField(null=True, blank=True)
    unidad_funcionalActual = models.IntegerField(null=True, blank=True)

    expediente = models.IntegerField(null=True, blank=True )
    plano = models.IntegerField(null=True, blank=True)
    TomoCatastral = models.IntegerField(null=True, blank=True)
    folioCatastral = models.ImageField(null=True, blank=True)

    apellido = models.CharField(max_length=255, null=True, blank=True)
    calle = models.CharField(max_length=255, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
  
    cuit = models.CharField(max_length=255, null=True, blank=True)
    tomoJuridicos = models.CharField(max_length=255, null=True, blank=True)
    FolioJuridicos = models.CharField(max_length=255, null=True, blank=True)
    matricula = models.CharField(max_length=50, null=True, blank=True)
    fecha_juridicos = models.DateField(null=True, blank=True)
    fecha_matricula = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Formulario de {self.usuario.username}"
        
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