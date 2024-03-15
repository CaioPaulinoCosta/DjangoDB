from django.shortcuts import render, redirect  # Adicionei 'redirect'
from sum_app.models import Cliente
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def index(request):
    lista_itens = Cliente.objects.all()

    # Verifica se há clientes cadastrados
    if lista_itens.exists():
        return render(request, 'users.html', {'lista_itens': lista_itens})
    else:
        return redirect('register_page')  # Redireciona para 'register_page' se não houver clientes cadastrados

def register_page(request):
    return render(request, 'register.html')

@csrf_exempt
def ClienteForm(request):
    register = {}  
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento') 
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        
        idade = calcular_idade(data_nascimento)
        novo_cliente = Cliente.objects.create(nome=nome, idade=idade, email=email, telefone=telefone, endereco=endereco)
        lista_itens = Cliente.objects.all()
        return render(request, 'users.html', {'lista_itens': lista_itens, 'nome': nome, 'idade': idade, 'email': email, 'telefone': telefone, 'endereco': endereco, 'register': register})
    lista_itens = Cliente.objects.all()
    return render(request, 'users.html', {'lista_itens': lista_itens, 'register': register})

def calcular_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year
    if data_atual.month < data_nascimento.month or (data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
        idade -= 1
    return idade
