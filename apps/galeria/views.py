from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.models import Fotografia

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não autenticado!')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não autenticado!')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if 'buscar' in request.GET:
        name_a_buscar = request.GET['buscar']
        # conferindo o nome
        if name_a_buscar:
            # verificando se algum card confere com o nome
            fotografias = fotografias.filter(nome__icontains= name_a_buscar)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})