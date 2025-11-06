from decimal import Decimal
from django.conf import settings
from apps.productos.models import Producto


class Carrito:
    """Clase para manejar el carrito de compras en sesiones"""
    
    def __init__(self, request):
        """Inicializar el carrito"""
        self.session = request.session
        carrito = self.session.get(settings.CART_SESSION_ID)
        
        if not carrito:
            # Crear un carrito vacío en la sesión
            carrito = self.session[settings.CART_SESSION_ID] = {}
        
        self.carrito = carrito
    
    def agregar(self, producto, cantidad=1, actualizar_cantidad=False):
        """
        Agregar un producto al carrito o actualizar su cantidad
        """
        producto_id = str(producto.id)
        
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {
                'cantidad': 0,
                'precio': str(producto.precio)
            }
        
        if actualizar_cantidad:
            self.carrito[producto_id]['cantidad'] = cantidad
        else:
            self.carrito[producto_id]['cantidad'] += cantidad
        
        self.guardar()
    
    def guardar(self):
        """Marcar la sesión como modificada para asegurar que se guarde"""
        self.session.modified = True
    
    def eliminar(self, producto):
        """Eliminar un producto del carrito"""
        producto_id = str(producto.id)
        
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar()
    
    def actualizar_cantidad(self, producto_id, cantidad):
        """Actualizar la cantidad de un producto"""
        producto_id = str(producto_id)
        
        if producto_id in self.carrito:
            if cantidad > 0:
                self.carrito[producto_id]['cantidad'] = cantidad
            else:
                del self.carrito[producto_id]
            self.guardar()
    
    def __iter__(self):
        """Iterar sobre los items del carrito y obtener los productos de la BD"""
        productos_ids = self.carrito.keys()
        productos = Producto.objects.filter(id__in=productos_ids)
        carrito = self.carrito.copy()
        
        for producto in productos:
            carrito[str(producto.id)]['producto'] = producto
        
        for item in carrito.values():
            item['precio'] = Decimal(item['precio'])
            item['total'] = item['precio'] * item['cantidad']
            yield item
    
    def __len__(self):
        """Contar todos los items en el carrito"""
        return sum(item['cantidad'] for item in self.carrito.values())
    
    def obtener_precio_total(self):
        """Calcular el precio total del carrito"""
        return sum(
            Decimal(item['precio']) * item['cantidad'] 
            for item in self.carrito.values()
        )
    
    def limpiar(self):
        """Limpiar el carrito de la sesión"""
        del self.session[settings.CART_SESSION_ID]
        self.guardar()
    
    def obtener_productos(self):
        """Obtener los productos del carrito"""
        productos_ids = self.carrito.keys()
        return Producto.objects.filter(id__in=productos_ids)# Carrito de compras
CART_SESSION_ID = 'carrito'