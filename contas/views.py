from django.shortcuts import render
from perfil.models import Categorias

def definir_contas(request):

    if request.method == 'GET':
        categorias = Categorias.objects.all()
        return render(request, 'definir_contas.html', {'categorias': categorias})