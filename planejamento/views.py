from django.shortcuts import render

def definir_planejamento(request):
    categorias = Categorias.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})
