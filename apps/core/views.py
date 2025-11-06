from django.shortcuts import render

def index(request):
    """Página principal"""
    return render(request, 'core/index.html')

def nosotros(request):
    """Página sobre nosotros"""
    return render(request, 'core/nosotros.html')

def contacto(request):
    """Página de contacto"""
    return render(request, 'core/contacto.html')