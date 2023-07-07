from django.shortcuts import render

def definir_contas(request):
    if request.method == 'GET':
        return render(request, 'definir_contas.html')