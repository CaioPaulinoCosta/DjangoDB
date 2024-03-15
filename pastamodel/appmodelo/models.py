# appmodelo/models.py
from django.db import models

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
