from django.db import models
from django.contrib.auth.models import User

class Evento (models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True,null=True)
    dataEvento = models.DateTimeField(verbose_name='Data do Evento')
    dataCriacaoEvento = models.DateTimeField(verbose_name='Data de Criação do Evento',auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo