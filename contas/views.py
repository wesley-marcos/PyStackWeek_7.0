from django.shortcuts import render, redirect
from perfil.models import Categorias
from .models import ContaPagar
from django.contrib import messages
from django.contrib.messages import constants

def definir_contas(request):

    if request.method == 'GET':
        categorias = Categorias.objects.all()
        return render(request, 'definir_contas.html', {'categorias': categorias})
    
    else:
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        dia_pagamento = request.POST.get('dia_pagamento')

        conta = ContaPagar(
            titulo=titulo,
            categoria_id=categoria,
            descricao=descricao,
            valor=valor,
            dia_pagamento=dia_pagamento
        )

        conta.save()

        messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso')
        return redirect('/contas/definir_contas')