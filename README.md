<div align="left">

# Sistema de Biblioteca en Línea   

Un sistema de gestión de biblioteca en línea construido con Django.

</div>

### Clonando el repositorio

--> Clona el repositorio usando el siguiente comando:

```bash
git clone https://github.com/tuusuario/E-library-System.git

--> Ingresa al directorio donde se encuentran los archivos del proyecto:

cd nombre_del_directorio

--> Crea un entorno virtual:

# Primero, instalamos virtualenv
pip install virtualenv

# Luego, creamos el entorno virtual
virtualenv nombre_del_entorno

--> Activa el entorno virtual:

nombre_del_entorno\scripts\activate

--> Instala los requerimientos:

pip install -r requirements.txt

Ejecutando la aplicación

--> Para ejecutar la aplicación, usamos:

python manage.py runserver

    Luego, el servidor de desarrollo se iniciará en http://127.0.0.1:8000/

Base de datos usando PostgreSQL
Características o módulos disponibles:

    API integrada creada con Django REST Framework (DRF)

    Cita aleatoria generada por la API para los usuarios

    Los usuarios pueden buscar libros por título, autor y categoría

    Existe un límite máximo (3) sobre cuántos libros puede tomar un usuario al mismo tiempo

    Existe un límite máximo (14) sobre cuántos días un usuario puede mantener un libro

    Los usuarios pueden reservar libros que no están disponibles actualmente y recibir una notificación por correo electrónico cuando el libro esté disponible nuevamente

    Se envía un correo electrónico con los detalles del libro que un usuario ha tomado prestado

    Función de recuperación de contraseña disponible

    Panel de administración para gestionar usuarios, libros, categorías y libros reservados
