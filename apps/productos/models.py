from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    """Modelo para las categorías de productos"""
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='categorias/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    orden = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['orden', 'nombre']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Modelo para los productos"""
    # Información básica
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    descripcion = models.TextField()
    descripcion_corta = models.CharField(max_length=300, blank=True)
    
    # Precios e inventario
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, 
                                         help_text="Precio antes del descuento")
    stock = models.IntegerField(default=0)
    
    # Detalles técnicos
    marca = models.CharField(max_length=100, blank=True)
    modelo = models.CharField(max_length=100, blank=True)
    codigo_producto = models.CharField(max_length=50, unique=True, blank=True, null=True)
    
    # Imágenes
    imagen_principal = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagen_2 = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagen_3 = models.ImageField(upload_to='productos/', blank=True, null=True)
    imagen_4 = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    # Estado y destacados
    disponible = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False, help_text="Mostrar en página principal")
    nuevo = models.BooleanField(default=False)
    
    # Metadata
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    vistas = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_creacion']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        
        # Si no hay código, guardar primero para obtener el ID
        if not self.codigo_producto:
            # Guardar sin código primero
            super().save(*args, **kwargs)
            # Generar código basado en el ID
            self.codigo_producto = f"ALM-{self.id:05d}"
            # Guardar nuevamente con el código
            super().save(update_fields=['codigo_producto'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    @property
    def tiene_descuento(self):
        """Verifica si el producto tiene descuento"""
        return self.precio_anterior and self.precio_anterior > self.precio

    @property
    def porcentaje_descuento(self):
        """Calcula el porcentaje de descuento"""
        if self.tiene_descuento:
            descuento = ((self.precio_anterior - self.precio) / self.precio_anterior) * 100
            return round(descuento)
        return 0

    @property
    def esta_en_stock(self):
        """Verifica si hay stock disponible"""
        return self.stock > 0

    def incrementar_vistas(self):
        """Incrementa el contador de vistas"""
        self.vistas += 1
        self.save(update_fields=['vistas'])