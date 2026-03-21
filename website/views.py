from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def atracoes(request):
    return render(request, 'website/atracoes.html')

def historia(request):
    return render(request, 'website/historia.html')

def galeria(request):
    return render(request, 'website/galeria.html')
