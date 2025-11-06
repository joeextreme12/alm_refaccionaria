from django.shortcuts import render
from apps.productos.models import Producto

def index(request):
    """Página principal"""
    # Obtener productos destacados
    productos_destacados = Producto.objects.filter(
        disponible=True,
        destacado=True
    )[:8]
    
    context = {
        'productos_destacados': productos_destacados
    }
    return render(request, 'core/index.html', context)

def nosotros(request):
    """Página sobre nosotros"""
    return render(request, 'core/nosotros.html')

def contacto(request):
    """Página de contacto"""
    return render(request, 'core/contacto.html')