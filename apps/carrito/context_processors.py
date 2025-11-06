from .carrito import Carrito


def carrito(request):
    """Context processor para tener el carrito disponible en todos los templates"""
    return {'carrito': Carrito(request)}