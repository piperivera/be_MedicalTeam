from django.db import models
from .usuario import Usuario

class Medico(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name= 'medico', on_delete=models.CASCADE)
    espcialidad = models.CharField('Especialidad',max_length=45)

