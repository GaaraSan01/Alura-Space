from django.urls import path
from apps.galeria.views import index, imagem, buscar, nova_imagem, delete_imagem, editar_imagem, filtro

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    path('deletar-imagem/<int:foto_id>', delete_imagem, name='delete_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
]