from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

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

    return render(request, 'galeria/index.html', {'cards': fotografias})


def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')

    return render(request, 'galeria/newpost.html', {'form': form})

def delete_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Post deletado com sucesso!')
    return redirect('index')

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            print(request.POST)
            form.save()
            messages.success(request, 'Fotografia editada com sucesso')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form':form, 'foto_id': foto_id})

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})