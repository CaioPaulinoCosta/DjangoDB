from django.db import models

class Comentario(models.Model):
    
    id = models.Autofield(primary_key=True)
    titulo = models.CharField(max_lenght=100)
    texto = models.TextField()
    data = model.DataTimeField(auto_now_add=True)
    hora = model.TimeField(auto_now_add=True)
    