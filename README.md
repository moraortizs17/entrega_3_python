# entrega_final_python

Descripción del proyecto:

1. Este proyecto se basa en una tienda virtual de ropa en la cual los usuarios podrá entrar, ver el catalogo de productos, elegir uno y por último comprar.
Asimismo, contamos cada registro de las personas que compran dentro de la plataforma, logrando captar información esencial para la realización de sus entregas.
También hemos creado un sistema de login y registro que le permite a los usuarios crear un perfil con nosotros usando su nombre, apellido, usuario, correo, teléfono y contraseña; una app de mensajeria que permite la comunicación entre los usuarios registrados en la página a través de mensajes de texto y un sistema que identifica si eres o no un usuario registrado para decidir qué modelos mostrarte, también elije qué puedes crear y editar.


2. Para usar este proyecto, se debe se tener instalado Python, uv y con esta misma agregar Django y las dependencias del requirements.txt

3. ¿Cómo correr este proyecto?:
   - Instalar dependencias: uv sync
   - Crear superusuario: uv run python manage.py createsuperuser
   - Correr uv run python manage.py makemigrations
   - Correr uv run python manage.py migrate
   - Correr el servidor: uv run python manage.py runserver
   - Entrar al admin en: http://127.0.0.1:8000/admin/

4. Las Urls para este proyecto son las siguientes y están dividivas por apps


App Store: 

Aquí las presento de manera mas organizada:
- http://127.0.0.1:8000/ - Inicio
- http://127.0.0.1:8000/productos/ - Lista de productos
- http://127.0.0.1:8000/clientes/ - Lista de clientes
- http://127.0.0.1:8000/ordenes/ - Lista de órdenes
- http://127.0.0.1:8000/categorias/ - Lista de categorías
- http://127.0.0.1:8000/about/ - Acerca de la tienda
- http://127.0.0.1:8000/productos/<id>/ - Detalle del producto
- http://127.0.0.1:8000/productos/crear/ - Crear un producto
- http://127.0.0.1:8000/productos/<id>/borrar/ - Borrar un producto
- http://127.0.0.1:8000/productos/<id>/editar/ - Editar un producto

App Cuenta:

- http://127.0.0.1:8000/cuentas/registro/ - Registro
- http://127.0.0.1:8000/cuentas/login/ - Login
- http://127.0.0.1:8000/cuentas/logout/ - Logout
- http://127.0.0.1:8000/cuentas/perfil/ - Perfil
- http://127.0.0.1:8000/cuentas/editar_perfil/ - Editar perfil
- http://127.0.0.1:8000/cuentas/cambiar_password/ - Cambio de contraseña

App Mensajeria

- http://127.0.0.1:8000/mensajeria/recibidos/ - Mensajes recibidos
- http://127.0.0.1:8000/mensajeria/enviados/ - Mensajes enviados
- http://127.0.0.1:8000/mensajeria/enviar_mensaje/ - Enviar un mensaje

Administrador de Django

- http://127.0.0.1:8000/admin/ - Panel de administración

5. En el proyecto encontramos 6 modelos en total:
- Productos: Modelo para guardar la información de los productos
- Ordenes: Modelo que guarda las ordenes realizadas por los clientes
- Clientes: Modelo dedicado a agregar clientes en la base de datos
- Categorías: Se conecta con productos, cada producto está asociado con una categoría
- Perfil: Para diferenciar entre usuarios se creó este modelo y se hizo una parte de este con "from django.contrib.auth.models import user" con el fin de crear un formulario de manera más rápida y sencilla
- Mensaje: Contamos con 4 variables, el remitente, el destinatario, el mensaje y la fecha de envio