from django.shortcuts import render, redirect
from perfil.models import Categorias, Conta
from .models import Valores
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime

def novo_valor(request):

    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categorias.objects.all()
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    
    elif request.method == "POST":
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')

        valores = Valores(
            valor=valor,
            categoria_id=categoria,
            descricao=descricao,
            data=data,
            conta_id=conta,
            tipo=tipo,
        )

        valores.save()

        conta = Conta.objects.get(id=conta)

        if tipo == "E":
            conta.valor += int(valor)
            messages.add_message(request, constants.SUCCESS, 'Entrada cadastrada com sucesso')    

        elif tipo == "S":
            conta.valor -= int(valor)
            messages.add_message(request, constants.SUCCESS, 'Saída cadastrada com sucesso')
        
        conta.save()

        return redirect('/extrato/novo_valor')
    
def view_extrato(request):

    valores = Valores.objects.filter(data__month=datetime.now().month)
    return render(request, 'view_extrato.html', {'valores': valores})