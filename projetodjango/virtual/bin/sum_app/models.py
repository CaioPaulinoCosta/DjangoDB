# appmodelo/models.py
from django.db import models

 
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.TextField(max_length=100)
    endereco = models.TextField(max_length=100)
    
def __str__(self):
    return self.nome

class ItemPedido(models.Model):
    id = models.AutoField(primary_key=True)
    nomeItem = models.CharField(max_length=100)
    quantidadeItem = models.CharField(max_length=100)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
def __str__(self):
    return self.nomeItem

    