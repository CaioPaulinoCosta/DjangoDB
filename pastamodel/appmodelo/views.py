from django.shortcuts import render
from appmodelo.models import Comentario

def index(request):
    lista_itens = Comentario.objects.all()
    return render(request, 'appmodelo/index.html', {'lista_itens':lista_itens})
    


