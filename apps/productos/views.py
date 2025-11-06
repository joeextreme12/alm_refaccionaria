from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Producto, Categoria

def catalogo(request):
    """Vista del catálogo de productos"""
    productos = Producto.objects.filter(disponible=True).select_related('categoria')
    categorias = Categoria.objects.filter(activo=True)
    
    # Filtrar por categoría
    categoria_slug = request.GET.get('categoria')
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        productos = productos.filter(categoria=categoria)
    
    # Filtrar por búsqueda
    query = request.GET.get('q')
    if query:
        productos = productos.filter(nombre__icontains=query) | productos.filter(descripcion__icontains=query)
    
    # Ordenamiento
    orden = request.GET.get('orden', '-fecha_creacion')
    productos = productos.order_by(orden)
    
    # Paginación
    paginator = Paginator(productos, 12)  # 12 productos por página
    page_number = request.GET.get('page')
    productos_paginados = paginator.get_page(page_number)
    
    context = {
        'productos': productos_paginados,
        'categorias': categorias,
        'categoria_actual': categoria_slug,
        'query': query,
    }
    return render(request, 'productos/catalogo.html', context)


def detalle_producto(request, slug):
    """Vista del detalle de un producto"""
    producto = get_object_or_404(Producto, slug=slug, disponible=True)
    
    # Incrementar vistas
    producto.incrementar_vistas()
    
    # Productos relacionados (misma categoría)
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria,
        disponible=True
    ).exclude(id=producto.id)[:4]
    
    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
    }
    return render(request, 'productos/detalle.html', context)


def buscar_productos(request):
    """Vista de búsqueda de productos"""
    query = request.GET.get('q', '')
    productos = []
    
    if query:
        productos = Producto.objects.filter(
            disponible=True
        ).filter(
            nombre__icontains=query
        ) | Producto.objects.filter(
            descripcion__icontains=query
        )
    
    context = {
        'query': query,
        'productos': productos,
    }
    return render(request, 'productos/buscar.html', context)