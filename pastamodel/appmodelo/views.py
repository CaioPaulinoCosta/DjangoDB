from django.shortcuts import render
from appmodelo.models import Comentario

def index(request):
    lista_itens = Comentario.objects.all()
    return render(request, 'index.html', ('lista_itens': lista_itens))

# Create your views here.
