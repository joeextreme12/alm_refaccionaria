# ALM Refaccionaria - E-commerce

Sistema de comercio electrónico desarrollado en Django para la venta de suspensiones y componentes automotrices.

## 🚀 Características

- **Landing Page moderna** con diseño responsive
- **Catálogo de productos** con filtros por categoría y búsqueda
- **Sistema de carrito de compras** con sesiones
- **Panel de administración** completo para gestionar productos
- **Checkout** con formulario de datos de envío
- **Diseño responsive** para móviles y tablets

## 📋 Requisitos

- Python 3.11+
- Django 5.2+
- Pillow (para manejo de imágenes)

## 🔧 Instalación

1. **Clonar el repositorio**
```bash
cd C:\xampp\htdocs
cd alm_refaccionaria
```

2. **Crear entorno virtual**
```bash
python -m venv venv
```

3. **Activar entorno virtual**
```bash
# Windows
.\venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

4. **Instalar dependencias**
```bash
pip install django pillow
```

5. **Crear migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crear superusuario**
```bash
python manage.py createsuperuser
```

7. **Iniciar servidor**
```bash
python manage.py runserver
```

8. **Acceder a la aplicación**
- Sitio web: http://127.0.0.1:8000/
- Panel admin: http://127.0.0.1:8000/admin/

## 📁 Estructura del Proyecto

```
alm_refaccionaria/
├── apps/
│   ├── core/           # Páginas principales (inicio, nosotros, contacto)
│   ├── productos/      # Sistema de productos y catálogo
│   └── carrito/        # Sistema de carrito de compras
├── config/             # Configuración de Django
├── static/             # Archivos estáticos (CSS, JS, imágenes)
├── media/              # Archivos subidos (imágenes de productos)
└── templates/          # Templates globales
```

## 🎨 Funcionalidades

### Para Usuarios
- Navegar por el catálogo de productos
- Filtrar productos por categoría
- Buscar productos
- Ver detalles de productos
- Agregar productos al carrito
- Modificar cantidades en el carrito
- Proceso de checkout

### Para Administradores
- Gestionar categorías de productos
- Agregar, editar y eliminar productos
- Gestionar inventario (stock)
- Configurar precios y descuentos
- Subir imágenes de productos
- Marcar productos como destacados o nuevos

## 🛠️ Tecnologías Utilizadas

- **Backend:** Django 5.2
- **Base de datos:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript
- **Iconos:** Font Awesome
- **Fuentes:** Google Fonts (Poppins)

## 📱 Páginas Disponibles

- `/` - Página de inicio
- `/nosotros/` - Sobre nosotros
- `/contacto/` - Contacto
- `/productos/` - Catálogo de productos
- `/productos/<slug>/` - Detalle de producto
- `/carrito/` - Ver carrito
- `/carrito/checkout/` - Finalizar compra
- `/admin/` - Panel de administración

## 👤 Uso del Panel de Administración

1. Acceder a `/admin/`
2. Iniciar sesión con las credenciales del superusuario
3. Gestionar productos y categorías

### Agregar Productos
1. Ir a "Productos" > "Agregar producto"
2. Completar información básica (nombre, categoría, descripción)
3. Establecer precio y stock
4. Subir imágenes
5. Marcar como destacado si se desea mostrar en la página principal
6. Guardar

## 🎯 Próximas Mejoras

- [ ] Sistema de usuarios y login
- [ ] Historial de pedidos
- [ ] Sistema de pago en línea
- [ ] Notificaciones por email
- [ ] Sistema de cupones de descuento
- [ ] Reviews y calificaciones de productos
- [ ] Integración con APIs de envío

## 📄 Licencia

Este proyecto es de uso educativo.

## 👨‍💻 Autor

Desarrollado para ALM Refaccionaria