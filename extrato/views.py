from django.shortcuts import render
from perfil.models import Categorias, Conta

def novo_valor(request):
    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categorias.objects.all()
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})