from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Tablero(models.Model):
    titulo_tablero = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tableros", null=True)

    def __str__(self):
        return self.titulo_tablero

class Task(models.Model):
    STATES = [('a','En proceso'),
              ('b','Pendiente'),
              ('c','Cancelada'),
              ('d','Finalizada')]
    
    task_name = models.CharField(max_length=100)
    task_description = models.CharField(max_length=100)
    task_status = models.CharField(max_length=1, choices=STATES, default='a')
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE, related_name="tablero_tareas", null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks", null=True)
    
    def __str__(self):
        return self.task_name
    
    