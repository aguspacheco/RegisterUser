from django.db import models

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