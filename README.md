# Sistema de Biblioteca Digital

Este repositorio contiene el código fuente de un sistema de biblioteca digital desarrollado con Django. El sistema permite gestionar libros, autores, categorías, préstamos, reservas y búsquedas de contenido, optimizando la administración y acceso a los recursos bibliográficos de manera eficiente y moderna.

---

## Tabla de Contenidos

- [Introducción](#introducción)
- [Características](#características)
- [Arquitectura](#arquitectura)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Guía de Instalación](#guía-de-instalación)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Introducción

El Sistema de Biblioteca Digital es una aplicación web para gestionar bibliotecas en línea, facilitando la búsqueda, préstamo y reserva de libros. Permite a los usuarios consultar información detallada de libros, autores y categorías, además de gestionar los préstamos con límites y notificaciones, mejorando así la experiencia de acceso y administración de la biblioteca.

---

## Características

- **Gestión de Libros**
  - Registro y edición de libros con información detallada: título, autor, categoría, fecha de publicación, imagen y descripción.
  - Control de stock y cantidad disponible.

- **Gestión de Autores y Categorías**
  - Registro y administración de autores y categorías de libros.

- **Préstamos y Reservas**
  - Registro de libros prestados a usuarios con límites de cantidad y tiempo.
  - Reservas de libros no disponibles y notificaciones por correo al regresar.

- **Búsqueda y Filtros**
  - Búsqueda de libros por título, autor o categoría.
  - Límite máximo de libros a prestar por usuario (3 libros).
  - Límite de préstamo por 14 días.

- **Notificaciones**
  - Envío automático de correos electrónicos con detalles de libros prestados y avisos de retorno.

- **Seguridad**
  - Sistema de autenticación y recuperación de contraseña para usuarios.

---

## Arquitectura

El sistema está construido con una arquitectura MVC (Modelo-Vista-Controlador) propia de Django, con separación clara entre lógica de negocio, datos y presentación.

- **Modelos:** Representan libros, autores, categorías, préstamos, reservas y búsquedas.
- **Vistas:** Controlan la interacción y respuesta a las solicitudes HTTP.
- **Templates:** Plantillas HTML para renderizar la interfaz de usuario.
- **API:** Endpoints RESTful para acceso programático usando Django REST Framework.

---

## Tecnologías Utilizadas

- **Backend:**
  - Python 3.10
  - Django 4.0.1
  - Django REST Framework
  - PostgreSQL (Base de datos)

- **Frontend:**
  - HTML5, CSS3, Bootstrap 4

- **Otros:**
  - django-crispy-forms para formularios
  - django-session-timeout para manejo de sesión
  - Librerías para envío de correo y manejo de imágenes

---

## Guía de Instalación

### Requisitos Previos

- Python 3.10 o superior
- PostgreSQL instalado y configurado
- Git

### Pasos para la instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

    Crear y activar un entorno virtual:

python -m venv env
source env/bin/activate  # En Linux/Mac
env\Scripts\activate     # En Windows

    Instalar dependencias:

pip install -r requirements.txt

    Configurar la base de datos PostgreSQL y actualizar settings.py con las credenciales.

    Ejecutar migraciones para crear tablas:

python manage.py makemigrations
python manage.py migrate

    Crear usuario administrador:

python manage.py createsuperuser

    Iniciar el servidor de desarrollo:

python manage.py runserver

Instrucciones de Uso

    Acceder a la aplicación en http://127.0.0.1:8000/

    Iniciar sesión o registrarse para usar funcionalidades completas.

    Navegar y buscar libros, ver detalles, realizar préstamos o reservas.

    Los administradores pueden gestionar libros, autores, categorías y usuarios desde el panel de administración.

Capturas de Pantalla


Vista principal de búsqueda y listado de libros


Página de detalle con información y opciones de préstamo
