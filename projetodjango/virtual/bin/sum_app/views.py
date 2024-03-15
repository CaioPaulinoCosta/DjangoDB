from django.shortcuts import render
from sum_app.models import Cliente
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def index(request):
    lista_itens = Cliente.objects.all()
    return render(request, 'result.html', {'lista_itens':lista_itens})

@csrf_exempt
def ClienteForm(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        
        print(f'nome: {nome}, idade: {idade}, email: {email}, telefone: {telefone}, endereco: {endereco}')
        return render(request, 'result.html', {'nome': nome, 'idade': idade, 'email': email, 'telefone': telefone,'endereco': endereco, 'result': result})
        
