from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from apps.productos.models import Producto
from .carrito import Carrito


def ver_carrito(request):
    """Vista para ver el carrito"""
    carrito = Carrito(request)
    
    # Calcular totales
    items = []
    for item in carrito:
        items.append(item)
    
    context = {
        'carrito': carrito,
        'items': items,
        'total': carrito.obtener_precio_total(),
    }
    return render(request, 'carrito/carrito.html', context)


@require_POST
def agregar_al_carrito(request, producto_id):
    """Agregar producto al carrito"""
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))
    
    # Verificar stock
    if cantidad > producto.stock:
        messages.error(request, f'Solo hay {producto.stock} unidades disponibles de {producto.nombre}')
        return redirect('productos:detalle', slug=producto.slug)
    
    carrito.agregar(producto=producto, cantidad=cantidad)
    messages.success(request, f'{producto.nombre} agregado al carrito')
    
    return redirect('carrito:ver_carrito')


@require_POST
def eliminar_del_carrito(request, producto_id):
    """Eliminar producto del carrito"""
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    messages.success(request, f'{producto.nombre} eliminado del carrito')
    
    return redirect('carrito:ver_carrito')


@require_POST
def actualizar_carrito(request, producto_id):
    """Actualizar cantidad de producto en el carrito"""
    carrito = Carrito(request)
    cantidad = int(request.POST.get('cantidad', 1))
    
    # Verificar stock
    producto = get_object_or_404(Producto, id=producto_id)
    if cantidad > producto.stock:
        messages.error(request, f'Solo hay {producto.stock} unidades disponibles')
        cantidad = producto.stock
    
    carrito.actualizar_cantidad(producto_id, cantidad)
    messages.success(request, 'Carrito actualizado')
    
    return redirect('carrito:ver_carrito')


def limpiar_carrito(request):
    """Limpiar todo el carrito"""
    carrito = Carrito(request)
    carrito.limpiar()
    messages.success(request, 'Carrito vaciado')
    
    return redirect('carrito:ver_carrito')


def checkout(request):
    """Vista del proceso de checkout"""
    carrito = Carrito(request)
    
    if len(carrito) == 0:
        messages.warning(request, 'Tu carrito está vacío')
        return redirect('productos:catalogo')
    
    # Calcular totales
    items = []
    for item in carrito:
        items.append(item)
    
    subtotal = carrito.obtener_precio_total()
    envio = Decimal('100.00')  # Costo fijo de envío
    total = subtotal + envio
    
    context = {
        'carrito': carrito,
        'items': items,
        'subtotal': subtotal,
        'envio': envio,
        'total': total,
    }
    
    if request.method == 'POST':
        # Aquí procesarías el pedido
        # Por ahora solo limpiamos el carrito
        messages.success(request, '¡Pedido realizado con éxito! Gracias por tu compra.')
        carrito.limpiar()
        return redirect('core:index')
    
    return render(request, 'carrito/checkout.html', context)


from decimal import Decimal