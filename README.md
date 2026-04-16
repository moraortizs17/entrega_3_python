# entrega_3_python

Descripción del proyecto:

1. Este proyecto se basa en una tienda virtual de ropa en la cual los usuarios podrá ntrar, ver el catalogo de productos, elegir uno y por último comprar.
Asimismo, contamos cada registro de las personas que compran dentro de la plataforma, logrando captar información esencial para la realización de sus entregas.

2. Para usar este proyecto, se debe se tener instalado Python, uv y con esta misma agregar Django

3. ¿Cómo correr este proyecto?:
   - Instalar dependencias: uv sync
   - Crear superusuario: uv run python manage.py createsuperuser
   - Correr el servidor: uv run python manage.py runserver
   - Entrar al admin en: http://127.0.0.1:8000/admin/

4. Las Urls para este proyecto se encuentran en la carpeta de componentes, en el archivo navbar.html
Cada una de estas urls te lleva a cada modelo para que pueda ser mostrado al usuario

Aquí las presento de manera mas organizada:
- http://127.0.0.1:8000/ — Inicio
- http://127.0.0.1:8000/productos/ — Lista de productos
- http://127.0.0.1:8000/clientes/ — Lista de clientes
- http://127.0.0.1:8000/ordenes/ — Lista de órdenes
- http://127.0.0.1:8000/categorias/ — Lista de categorías

5. En el proyecto encontramos 4 modelos en total:
- Productos: Modelo para guardar la información de los productos
- Ordenes: Modelo que guarda las ordenes realizadas por los clientes
- Clientes: Modelo dedicado a agregar clientes en la base de datos
- Categorías: Se conecta con productos, cada producto está asociado con una categoría