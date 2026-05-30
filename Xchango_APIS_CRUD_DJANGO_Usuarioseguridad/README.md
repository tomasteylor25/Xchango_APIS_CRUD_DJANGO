# API REST - Usuario Seguridad
API CRUD desarrollada con Django REST Framework para la gestión del esquema `Usuario_seguridad` en la base de datos `Xchango_db`.

---

## Tecnologías utilizadas
- Python 3.12
- Django 6.0
- Django REST Framework
- PostgreSQL
- psycopg2
- python-decouple

---

## Estructura del proyecto
```
usuario_seguridad_django/
├── .env
├── .gitignore
├── manage.py
├── run.py
├── backend/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── api/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── migrations/
```

---

## Base de datos
- **Base de datos:** `Xchango_db`
- **Esquema:** `Usuario_seguridad`

### Tablas
| Tabla | Descripción |
|---|---|
| `Usuario` | Datos principales del usuario (correo, estado, verificación) |
| `Credenciales` | Hash de contraseña, intentos fallidos y bloqueo |
| `Crear_contrasena` | Registro temporal de creación de contraseña |
| `HistorialContrasena` | Historial de contraseñas anteriores del usuario |
| `RecuperacionContrasena` | Tokens y códigos para recuperación de contraseña |
| `Sesion` | Sesiones activas con token, IP y user agent |
| `IntentoLogin` | Registro de intentos de inicio de sesión |
| `Perfil` | Datos personales del usuario (nombre, teléfono, municipio, etc.) |

---

## Instalación y ejecución

```bash
# 1. Activar el entorno virtual
venv\Scripts\activate

# 2. Instalar dependencias
pip install django djangorestframework drf-yasg psycopg2-binary python-decouple

# 3. Aplicar migraciones
python manage.py migrate

# 4. Correr el servidor
python run.py
```

---

## Endpoints disponibles

Base URL: `http://127.0.0.1:9000/api/`

| Método | Endpoint | Descripción |
|---|---|---|
| GET / POST | `/api/usuarios/` | Listar o crear usuarios |
| GET / PUT / DELETE | `/api/usuarios/{id}/` | Detalle, editar o eliminar un usuario |
| GET / POST | `/api/credenciales/` | Listar o crear credenciales |
| GET / PUT / DELETE | `/api/credenciales/{id}/` | Detalle, editar o eliminar credenciales |
| GET / POST | `/api/crear-contrasena/` | Listar o crear registro de contraseña |
| GET / PUT / DELETE | `/api/crear-contrasena/{id}/` | Detalle, editar o eliminar |
| GET / POST | `/api/historial-contrasena/` | Listar o crear historial |
| GET / PUT / DELETE | `/api/historial-contrasena/{id}/` | Detalle, editar o eliminar |
| GET / POST | `/api/recuperacion-contrasena/` | Listar o crear recuperación |
| GET / PUT / DELETE | `/api/recuperacion-contrasena/{id}/` | Detalle, editar o eliminar |
| GET / POST | `/api/sesiones/` | Listar o crear sesiones |
| GET / PUT / DELETE | `/api/sesiones/{id}/` | Detalle, editar o eliminar |
| GET / POST | `/api/intentos-login/` | Listar o crear intentos de login |
| GET / PUT / DELETE | `/api/intentos-login/{id}/` | Detalle, editar o eliminar |
| GET / POST | `/api/perfiles/` | Listar o crear perfiles |
| GET / PUT / DELETE | `/api/perfiles/{id}/` | Detalle, editar o eliminar |
