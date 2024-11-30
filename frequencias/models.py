from django.db import models
from django.contrib.auth.models import User
from users.models import Funcionario

# Create your models here.

class FrequenciaModel(models.Model):
    hora_inicio = models.DateTimeField()
    hora_fim = models.DateTimeField(null=True, blank=True)
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Funcionário: [{self.funcionario}] - Frequencia:[{self.hora_inicio}] - [{self.hora_fim}]'
    
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"