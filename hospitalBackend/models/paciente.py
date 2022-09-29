from django.db import models
from .usuario import Usuario
from .medico import Medico

class Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    medico = models.ForeignKey( Medico, on_delete=models.CASCADE)
    
    
