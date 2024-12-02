import sqlite3
from django.contrib.auth.models import User, Permission
from django.db import connection
from datetime import date, timedelta
from random import randint
from core.models import Categoria, Producto, Carrito, Perfil, Boleta, DetalleBoleta, Bodega

def eliminar_tabla(nombre_tabla):
    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM {nombre_tabla}")
    conexion.commit()
    conexion.close()

def exec_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

def crear_usuario(username, tipo, nombre, apellido, correo, es_superusuario, 
    es_staff, rut, direccion, subscrito, imagen):

    try:
        print(f'Verificar si existe usuario {username}.')

        if User.objects.filter(username=username).exists():
            print(f'   Eliminar {username}')
            User.objects.get(username=username).delete()
            print(f'   Eliminado {username}')
        
        print(f'Iniciando creación de usuario {username}.')

        usuario = None
        if tipo == 'Superusuario':
            print('    Crear Superuser')
            usuario = User.objects.create_superuser(username=username, password='123')
        else:
            print('    Crear User')
            usuario = User.objects.create_user(username=username, password='123')

        if tipo == 'Administrador':
            print('    Es administrador')
            usuario.is_staff = es_staff
            
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo
        usuario.save()

        if tipo == 'Administrador':
            print(f'    Dar permisos a core y apirest')
            permisos = Permission.objects.filter(content_type__app_label__in=['core', 'apirest'])
            usuario.user_permissions.set(permisos)
            usuario.save()
 
        print(f'    Crear perfil: RUT {rut}, Subscrito {subscrito}, Imagen {imagen}')
        Perfil.objects.create(
            usuario=usuario, 
            tipo_usuario=tipo,
            rut=rut,
            direccion=direccion,
            subscrito=subscrito,
            imagen=imagen)
        print("    Creado correctamente")
    except Exception as err:
        print(f"    Error: {err}")

def eliminar_tablas():
    eliminar_tabla('auth_user_groups')
    eliminar_tabla('auth_user_user_permissions')
    eliminar_tabla('auth_group_permissions')
    eliminar_tabla('auth_group')
    eliminar_tabla('auth_permission')
    eliminar_tabla('django_admin_log')
    eliminar_tabla('django_content_type')
    #eliminar_tabla('django_migrations')
    eliminar_tabla('django_session')
    eliminar_tabla('Bodega')
    eliminar_tabla('DetalleBoleta')
    eliminar_tabla('Boleta')
    eliminar_tabla('Perfil')
    eliminar_tabla('Carrito')
    eliminar_tabla('Producto')
    eliminar_tabla('Categoria')
    #eliminar_tabla('authtoken_token')
    eliminar_tabla('auth_user')

def poblar_bd(test_user_email=''):
    eliminar_tablas()

    crear_usuario(
        username='cevans',
        tipo='Cliente', 
        nombre='Chris', 
        apellido='Evans', 
        correo=test_user_email if test_user_email else 'cevans@marvel.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='25.747.200-0',	
        direccion='123 Main Street, Los Angeles, \nCalifornia 90001 \nEstados Unidos', 
        subscrito=True, 
        imagen='perfiles/cevans.jpg')

    crear_usuario(
        username='eolsen',
        tipo='Cliente', 
        nombre='Elizabeth', 
        apellido='Olsen', 
        correo=test_user_email if test_user_email else 'eolsen@marvel.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='12.202.357-5', 
        direccion='Albert Street, New York, \nNew York 10001 \nEstados Unidos', 
        subscrito=True, 
        imagen='perfiles/eolsen.jpg')

    crear_usuario(
        username='tholland',
        tipo='Cliente', 
        nombre='Tom', 
        apellido='Holland', 
        correo=test_user_email if test_user_email else 'tholland@marvel.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='11.991.600-3', 
        direccion='105 Apple Park Way, \nCupertino, CA 95014 \nEstados Unidos', 
        subscrito=False, 
        imagen='perfiles/tholland.jpg')

    crear_usuario(
        username='sjohansson',
        tipo='Cliente', 
        nombre='Scarlett', 
        apellido='Johansson', 
        correo=test_user_email if test_user_email else 'sjohansson@marvel.com', 
        es_superusuario=False, 
        es_staff=False, 
        rut='16.469.725-8', 
        direccion='350 5th Ave, \nNew York, NY 10118 \nEstados Unidos', 
        subscrito=False, 
        imagen='perfiles/sjohansson.jpg')

    crear_usuario(
        username='cpratt',
        tipo='Administrador', 
        nombre='Chris', 
        apellido='Pratt', 
        correo=test_user_email if test_user_email else 'cpratt@marvel.com', 
        es_superusuario=False, 
        es_staff=True, 
        rut='19.441.980-5', 
        direccion='10 Pine Road, Miami, \nFlorida 33101 \nEstados Unidos', 
        subscrito=False, 
        imagen='perfiles/cpratt.jpg')
    
    crear_usuario(
        username='mruffalo',
        tipo='Administrador', 
        nombre='Mark', 
        apellido='Ruffalo', 
        correo=test_user_email if test_user_email else 'mruffalo@marvel.com', 
        es_superusuario=False, 
        es_staff=True, 
        rut='21.708.052-5', 
        direccion='1600 Pennsylvania Avenue NW, \nWashington, D.C. \nEstados Unidos', 
        subscrito=False, 
        imagen='perfiles/mruffalo.jpg')

    crear_usuario(
        username='super',
        tipo='Superusuario',
        nombre='Robert',
        apellido='Downey Jr.',
        correo=test_user_email if test_user_email else 'rdowneyjr@marvel.com',
        es_superusuario=True,
        es_staff=True,
        rut='13.029.317-4',
        direccion='15 Oak Street, Los Angeles, \nCalifornia 90001 \nEstados Unidos',
        subscrito=False,
        imagen='perfiles/rdowneyjr.jpg')
    
    categorias_data = [
        { 'id': 1, 'nombre': 'Habitacion Familiar'},
        { 'id': 2, 'nombre': 'Aventura'},
        { 'id': 3, 'nombre': 'Estrategia'},
        { 'id': 4, 'nombre': 'RPG'},
    ]

    print('Crear categorías')
    for categoria in categorias_data:
        Categoria.objects.create(**categoria)
    print('Categorías creadas correctamente')

    productos_data = [
        # Categoría "Acción" (8 juegos)
        {
            'id': 1,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Hotel Paraíso Tropical',
            'descripcion': 'Sumérgete en la tranquilidad de nuestro oasis tropical. Habitaciones amplias con vistas al mar y servicios de lujo te esperan para ofrecerte una experiencia inolvidable.',
            'precio': 299990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000001.jpg'
        },
        {
            'id': 2,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Hotel Bella Vista',
            'descripcion': 'Disfruta de impresionantes panorámicas desde tu balcón privado en el corazón de la ciudad. Perfecto para viajeros de negocios y turistas, ofrecemos comodidad y elegancia.',
            'precio': 599990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000002.jpg'
        },
        {
            'id': 3,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Hotel Jardines del Sol',
            'descripcion': 'Un refugio sereno rodeado de exuberantes jardines. Relájate en nuestra piscina al aire libre y disfruta de una cocina exquisita en nuestro restaurante de alta categoría.',
            'precio': 699990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000003.jpg'
        },
        {
            'id': 4,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Hotel Maravilla Urbana',
            'descripcion': 'Ubicado en el centro de la ciudad, este hotel combina el encanto histórico con las comodidades modernas. Ideal para quienes desean explorar los principales puntos de interés.',
            'precio': 699990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 5,
            'imagen': 'productos/000004.jpg'
        },
        {
            'id': 5,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Hotel Montaña Serena',
            'descripcion': 'Escápate a la naturaleza y disfruta de actividades al aire libre como senderismo y pesca. Nuestras cabañas acogedoras ofrecen la escapada perfecta del bullicio de la ciudad.',
            'precio': 199990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 20,
            'imagen': 'productos/000005.jpg'
        },
        {
            'id': 6,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Hotel Costa Azul',
            'descripcion': 'Experimenta el lujo en la costa. Con acceso directo a la playa, un spa de clase mundial y restaurantes gourmet, tu estancia será inolvidable.',
            'precio': 599990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000006.jpg'
        },
        {
            'id': 7,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Hotel Estrella del Norte',
            'descripcion': 'Situado en un entorno montañoso, este hotel ofrece vistas espectaculares y un ambiente relajante. Ideal para esquiadores y amantes de la naturaleza.',
            'precio': 699990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000007.jpg'
        },
        {
            'id': 8,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Hotel Encanto del Valle',
            'descripcion': 'Ubicado en un pintoresco valle, disfruta de la tranquilidad y el confort. Perfecto para una escapada romántica o un retiro de bienestar.',
            'precio': 499990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000008.jpg'
        },
        # Categoría "Aventura" (4 juegos)
        {
            'id': 9,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Hotel Ciudadela Real',
            'descripcion': 'Vive como la realeza en nuestro castillo renovado. Con habitaciones temáticas y un ambiente histórico, tu estancia será única.',
            'precio': 599990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000009.jpg'
        },
        {
            'id': 10,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Hotel Playa Dorada',
            'descripcion': 'Un paraíso para los amantes de la playa. Habitaciones con vista al mar, actividades acuáticas y entretenimiento nocturno para toda la familia.',
            'precio': 199990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 20,
            'imagen': 'productos/000010.jpg'
        },
        {
            'id': 11,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Hotel Horizonte Claro',
            'descripcion': 'Un moderno hotel de negocios con todas las facilidades que necesitas para tu viaje de trabajo. Salas de conferencias, Wi-Fi rápido y un gimnasio bien equipado.',
            'precio': 599990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000011.jpg'
        },
        {
            'id': 12,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Hotel Cielo Nocturno',
            'descripcion': 'Descubre el romance bajo las estrellas en nuestras suites con techo de vidrio. Un lugar perfecto para celebrar aniversarios y ocasiones especiales.',
            'precio': 399990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000012.jpg'
        },
        # Categoría "Estrategia" (4 juegos)
        {
            'id': 13,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Hotel Oasis Urbano',
            'descripcion': 'Un refugio elegante en medio de la ciudad. Habitaciones de diseño contemporáneo, una piscina en la azotea y un bar con vistas impresionantes.',
            'precio': 399990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 5,
            'imagen': 'productos/000013.jpg'
        },
        {
            'id': 14,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Hotel Refugio Alpino',
            'descripcion': 'Escápate a la serenidad de los Alpes. Disfruta de actividades al aire libre durante el día y relájate en nuestro acogedor salón con chimenea por la noche.',
            'precio': 199990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000014.jpg'
        },
        {
            'id': 15,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Hotel Brisa Marina',
            'descripcion': 'Ubicado a pocos pasos del mar, este hotel ofrece una experiencia relajante con habitaciones cómodas y un servicio atento. Perfecto para unas vacaciones tranquilas.',
            'precio': 599990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000015.jpg'
        },
        {
            'id': 16,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Hotel Torre del Sol',
            'descripcion': 'Un hotel moderno con vistas espectaculares de la ciudad desde nuestra azotea. Disfruta de nuestra piscina infinita y un bar en la azotea.',
            'precio': 599990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000016.jpg'
        },
        # Categoría "RPG" (4 juegos)
        {
            'id': 17,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Hotel Jardines Secretos',
            'descripcion': 'Un encantador hotel boutique rodeado de exuberantes jardines. Ideal para una escapada romántica o un retiro tranquilo.',
            'precio': 299990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000017.jpg'
        },
        {
            'id': 18,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Hotel Vistas Eternas',
            'descripcion': 'Situado en un acantilado, ofrece vistas panorámicas al océano y un ambiente sereno. Perfecto para una escapada de relax y rejuvenecimiento.',
            'precio': 599990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 5,
            'imagen': 'productos/000018.jpg'
        },
        {
            'id': 19,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Hotel Palacio Escondido',
            'descripcion': 'Vive la historia en nuestro hotel boutique ubicado en un antiguo palacio. Cada habitación es única y está decorada con un estilo distintivo.',
            'precio': 399990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000019.jpg'
        },
        {
            'id': 20,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Hotel Rincón del Cielo',
            'descripcion': 'Disfruta de un servicio personalizado en un entorno exclusivo. Con solo unas pocas habitaciones, garantizamos una experiencia íntima y memorable.',
            'precio': 699990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000020.jpg'
        }
    ]

    print('Crear productos')
    for producto in productos_data:
        Producto.objects.create(**producto)
    print('Productos creados correctamente')

    print('Crear carritos')
    for rut in ['25.747.200-0', '11.991.600-3']:
        cliente = Perfil.objects.get(rut=rut)
        for cantidad_productos in range(1, 11):
            producto = Producto.objects.get(pk=randint(1, 10))
            if cliente.subscrito:
                descuento_subscriptor = producto.descuento_subscriptor
            else:
                descuento_subscriptor = 0
            descuento_oferta = producto.descuento_oferta
            descuento_total = descuento_subscriptor + descuento_oferta
            descuentos = int(round(producto.precio * descuento_total / 100))
            precio_a_pagar = producto.precio - descuentos
            Carrito.objects.create(
                cliente=cliente,
                producto=producto,
                precio=producto.precio,
                descuento_subscriptor=descuento_subscriptor,
                descuento_oferta=descuento_oferta,
                descuento_total=descuento_total,
                descuentos=descuentos,
                precio_a_pagar=precio_a_pagar
            )
    print('Carritos creados correctamente')

    print('Crear boletas')
    nro_boleta = 0
    perfiles_cliente = Perfil.objects.filter(tipo_usuario='Cliente')
    for cliente in perfiles_cliente:
        estado_index = -1
        for cant_boletas in range(1, randint(6, 21)):
            nro_boleta += 1
            estado_index += 1
            if estado_index > 3:
                estado_index = 0
            estado = Boleta.ESTADO_CHOICES[estado_index][1]
            fecha_venta = date(2023, randint(1, 5), randint(1, 28))
            fecha_despacho = fecha_venta + timedelta(days=randint(0, 3))
            fecha_entrega = fecha_despacho + timedelta(days=randint(0, 3))
            if estado == 'Anulado':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Vendido':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Despachado':
                fecha_entrega = None
            boleta = Boleta.objects.create(
                nro_boleta=nro_boleta, 
                cliente=cliente,
                monto_sin_iva=0,
                iva=0,
                total_a_pagar=0,
                fecha_venta=fecha_venta,
                fecha_despacho=fecha_despacho,
                fecha_entrega=fecha_entrega,
                estado=estado)
            detalle_boleta = []
            total_a_pagar = 0
            for cant_productos in range(1, randint(4, 6)):
                producto_id = randint(1, 10)
                producto = Producto.objects.get(id=producto_id)
                precio = producto.precio
                descuento_subscriptor = 0
                if cliente.subscrito:
                    descuento_subscriptor = producto.descuento_subscriptor
                descuento_oferta = producto.descuento_oferta
                descuento_total = descuento_subscriptor + descuento_oferta
                descuentos = int(round(precio * descuento_total / 100))
                precio_a_pagar = precio - descuentos
                bodega = Bodega.objects.create(producto=producto)
                DetalleBoleta.objects.create(
                    boleta=boleta,
                    bodega=bodega,
                    precio=precio,
                    descuento_subscriptor=descuento_subscriptor,
                    descuento_oferta=descuento_oferta,
                    descuento_total=descuento_total,
                    descuentos=descuentos,
                    precio_a_pagar=precio_a_pagar)
                total_a_pagar += precio_a_pagar
            monto_sin_iva = int(round(total_a_pagar / 1.19))
            iva = total_a_pagar - monto_sin_iva
            boleta.monto_sin_iva = monto_sin_iva
            boleta.iva = iva
            boleta.total_a_pagar = total_a_pagar
            boleta.fecha_venta = fecha_venta
            boleta.fecha_despacho = fecha_despacho
            boleta.fecha_entrega = fecha_entrega
            boleta.estado = estado
            boleta.save()
            print(f'    Creada boleta Nro={nro_boleta} Cliente={cliente.usuario.first_name} {cliente.usuario.last_name}')
    print('Boletas creadas correctamente')

    print('Agregar productos a bodega')
    for producto_id in range(1, 11):
        producto = Producto.objects.get(id=producto_id)
        cantidad = 0
        for cantidad in range(1, randint(2, 31)):
            Bodega.objects.create(producto=producto)
        print(f'    Agregados {cantidad} "{producto.nombre}" a la bodega')
    print('Productos agregados a bodega')

