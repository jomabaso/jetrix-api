from django.db import models

# Create your models here.
class Tablero(models.Model):
    titulo_tablero = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo_tablero
