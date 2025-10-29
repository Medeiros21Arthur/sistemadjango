from django.db import models
from usuarios.models import motoristas
class Gravacoes(models.Model):
    video = models.FileField(upload_to='gravacoes')
    data = models.DateTimeField()
    transcrever = models.BooleanField(default=False)
    motoristas = models.ForeignKey(motoristas, on_delete=models.DO_NOTHING)
    humor = models.IntegerField(default=0)
    transcricao = models.TextField()
    resumo = models.JSONField(default=list, blank=True)
    segmentos = models.JSONField(default=list, blank=True)