from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo', 'orden', 'fecha_creacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ['activo', 'orden']
    ordering = ['orden', 'nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'disponible', 'destacado', 'fecha_creacion']
    list_filter = ['disponible', 'destacado', 'nuevo', 'categoria', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion', 'codigo_producto', 'marca']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ['disponible', 'destacado', 'precio', 'stock']
    readonly_fields = ['vistas', 'fecha_creacion', 'fecha_actualizacion']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'slug', 'categoria', 'descripcion', 'descripcion_corta')
        }),
        ('Precios e Inventario', {
            'fields': ('precio', 'precio_anterior', 'stock')
        }),
        ('Detalles Técnicos', {
            'fields': ('marca', 'modelo', 'codigo_producto')
        }),
        ('Imágenes', {
            'fields': ('imagen_principal', 'imagen_2', 'imagen_3', 'imagen_4')
        }),
        ('Estado', {
            'fields': ('disponible', 'destacado', 'nuevo')
        }),
        ('Metadata', {
            'fields': ('vistas', 'fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('categoria')