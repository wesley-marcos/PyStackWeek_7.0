from django.shortcuts import render

def novo_valor(request):
    if request.method == "GET":
        return render(request, 'novo_valor.html')