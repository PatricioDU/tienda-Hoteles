# Tienda Hoteles

Plataforma de comercio electrónico construida con Django, con gestión de productos, inventario, carrito de compra y pago integrado con Transbank.

## Descripción

Tienda Hoteles es una aplicación web de e-commerce desarrollada en Django que permite a los usuarios navegar un catálogo de productos organizados por categorías, agregarlos al carrito y finalizar su pedido a través de un sistema de boletas con seguimiento del estado del despacho.

El sistema distingue tres tipos de usuario: cliente, administrador y superusuario. Los clientes con suscripción activa acceden a descuentos adicionales sobre el precio base, que se combinan con las promociones vigentes en cada producto. El módulo de bodega permite hacer seguimiento del inventario, y el ciclo de vida de cada boleta pasa por estados definidos: vendido, despachado, entregado y anulado. La integración con Transbank SDK permite procesar pagos reales con tarjeta, lo que hace al proyecto apto para un entorno de producción con las configuraciones adecuadas.

El proyecto también expone una API REST a través de Django REST Framework, pensada para integraciones con otros sistemas o frontends alternativos.

## Tecnologías

- Python 3
- Django 5.0
- Django REST Framework 3.15
- Transbank SDK 5.0
- Pillow (manejo de imágenes de productos)
- SQLite (entorno de desarrollo)
- SQL Server / Oracle (soporte comentado en settings para producción)
- pyodbc / mssql-django (conector para SQL Server)
- HTML, CSS, JavaScript (templates Django)

## Uso

### Requisitos previos

- Python 3.10 o superior
- pip

### Instalación

Clona el repositorio y accede a la carpeta del proyecto:

```bash
git clone https://github.com/PatricioDU/tienda-Hoteles.git
cd tienda-Hoteles
```

Crea y activa un entorno virtual. En Windows:

```bash
python -m venv myenv
myenv\Scripts\activate
```

En Linux o macOS:

```bash
python -m venv myenv
source myenv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

### Configuración

El archivo de configuración principal está en `tienda/settings.py`. Por defecto usa SQLite para desarrollo local, por lo que no necesitas configurar ninguna base de datos adicional para empezar. Si quieres conectar un motor diferente (SQL Server u Oracle), los bloques necesarios ya están disponibles en ese archivo como comentarios.

> Antes de llevar el proyecto a producción, asegúrate de mover la clave secreta y las credenciales de correo a variables de entorno y desactivar el modo `DEBUG`.

### Migración de la base de datos

```bash
python manage.py migrate
```

Para cargar datos de ejemplo en la base de datos, revisa el script `core/zpoblar.py` y ejecútalo si lo necesitas.

### Ejecución

```bash
python manage.py runserver
```

La aplicación queda disponible en `http://localhost:8000`.

Para acceder al panel de administración de Django, crea primero un superusuario:

```bash
python manage.py createsuperuser
```

Luego entra en `http://localhost:8000/admin`.
