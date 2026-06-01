# Xchango API — Módulo Sistema

API REST CRUD para el módulo de administración del sistema **Xchango**, desarrollada en **Django 6 + Django REST Framework + PostgreSQL**.

---

## Tecnologías

| Paquete | Versión |
|---|---|
| Python | 3.14 |
| Django | 6.0.5 |
| djangorestframework | 3.17.1 |
| drf-yasg | 1.21.15 |
| psycopg2-binary | 2.9.12 |
| python-decouple | 3.x |
| openpyxl | 3.x |

---

## Estructura del proyecto

xchango_django/
├── .env                    ← Variables de entorno (NO subir al repo)
├── .gitignore
├── manage.py
├── run.py                  ← Atajo para correr el servidor
├── backen/
│   ├── init.py
│   ├── settings.py         ← Configuración del proyecto
│   ├── urls.py             ← Rutas raíz + Swagger
│   ├── asgi.py
│   └── wsgi.py
└── api/
├── init.py
├── apps.py
├── models.py           ← 6 modelos del esquema 'sistema'
├── serializers.py      ← Serializadores de cada modelo
├── views.py            ← ViewSets CRUD + exportación Excel
├── urls.py             ← Enrutador con los 6 recursos
├── admin.py
├── tests.py
└── migrations/
└── init.py

---

## Instalación

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
venv\Scripts\activate.bat

# 3. Instalar dependencias
pip install django djangorestframework psycopg2-binary drf-yasg python-decouple setuptools openpyxl
```

---

## Variables de entorno (.env)

Crea un archivo `.env` en la raíz del proyecto con los siguientes valores:

```env
DB_NAME=*****
DB_USER=*****
DB_PASSWORD=*
DB_HOST=*****
DB_PORT=*****
DB_SCHEMA=***
```

---

## Correr el servidor

```bash
python run.py
```

El servidor inicia en:

http://127.0.0.1:8081/

> **Importante:** NO ejecutes `makemigrations` ni `migrate`. Las tablas ya existen en PostgreSQL. Django simplemente las usa.

---

## Endpoints

Todos los endpoints tienen el prefijo `/sistema/`.

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/sistema/{recurso}/` | Listar todos los registros |
| `POST` | `/sistema/{recurso}/` | Crear un nuevo registro |
| `GET` | `/sistema/{recurso}/{id}/` | Obtener un registro por ID |
| `PUT` | `/sistema/{recurso}/{id}/` | Actualizar un registro completo |
| `PATCH` | `/sistema/{recurso}/{id}/` | Actualizar un registro parcialmente |
| `DELETE` | `/sistema/{recurso}/{id}/` | Eliminar un registro |
| `GET` | `/sistema/{recurso}/excel/` | Exportar todos los registros a Excel |

---

## Recursos disponibles

| Modelo | Ruta | Tabla en BD |
|---|---|---|
| Nivel de Acceso | `/sistema/nivel_acceso/` | `nivel_acceso` |
| Permiso | `/sistema/permiso/` | `permiso` |
| Administrador | `/sistema/administrador/` | `administrador` |
| Administrador Permiso | `/sistema/administradorpermiso/` | `administradorpermiso` |
| Historial Admin | `/sistema/historialadmin/` | `historialadmin` |
| Notificación | `/sistema/notificacion/` | `notificacion` |

---

## Exportación de datos a Excel

Cada recurso dispone de un endpoint dedicado para descargar todos sus registros en formato `.xlsx`.

### Endpoints `/excel/`

| Recurso | URL de exportación |
|---|---|
| Nivel de Acceso | `/sistema/nivel_acceso/excel/` |
| Permiso | `/sistema/permiso/excel/` |
| Administrador | `/sistema/administrador/excel/` |
| Administrador Permiso | `/sistema/administradorpermiso/excel/` |
| Historial Admin | `/sistema/historialadmin/excel/` |
| Notificación | `/sistema/notificacion/excel/` |

### Características de la exportación

- Generación automática de archivos `.xlsx`
- Descarga directa desde el navegador
- Exportación de todos los registros disponibles
- Compatible con Excel, LibreOffice y Google Sheets

### Ejemplo de uso

```bash
GET http://127.0.0.1:8081/sistema/notificacion/excel/
```

### Descarga del archivo

Al acceder al endpoint `/excel/`, el servidor responde con las cabeceras HTTP necesarias para forzar la descarga automática del archivo en el navegador:

Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
Content-Disposition: attachment; filename="notificacion.xlsx"

---

## Modelos

### NivelAcceso
| Campo | Tipo | Descripción |
|---|---|---|
| id_nivelacceso | AutoField | Clave primaria |
| nombre | CharField(20) | Nombre del nivel |
| activo | BooleanField | Estado |
| fecha_asignacion | DateTimeField | Fecha de asignación |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### Permiso
| Campo | Tipo | Descripción |
|---|---|---|
| id_permiso | AutoField | Clave primaria |
| nombre | CharField(100) | Nombre del permiso |
| descripcion | TextField | Descripción opcional |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### Administrador
| Campo | Tipo | Descripción |
|---|---|---|
| id_admin | AutoField | Clave primaria |
| id_usuario | IntegerField | ID del usuario (FK externa) |
| id_nivelacceso | ForeignKey | Nivel de acceso asignado |
| activo | BooleanField | Estado |
| fecha_asignacion | DateTimeField | Fecha de asignación |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### AdministradorPermiso
| Campo | Tipo | Descripción |
|---|---|---|
| id | AutoField | Clave primaria |
| id_admin | ForeignKey | Administrador |
| id_permiso | ForeignKey | Permiso asignado |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### HistorialAdmin
| Campo | Tipo | Descripción |
|---|---|---|
| id_historial | AutoField | Clave primaria |
| id_admin | ForeignKey | Administrador que realizó la acción |
| accion | CharField(100) | Acción realizada |
| descripcion | TextField | Detalle opcional |
| tipo_objeto | CharField(50) | Tipo de objeto afectado |
| id_objeto | IntegerField | ID del objeto afectado |
| fecha_accion | DateTimeField | Fecha de la acción |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### Notificacion
| Campo | Tipo | Descripción |
|---|---|---|
| id_notificacion | AutoField | Clave primaria |
| id_usuario | IntegerField | ID del usuario destino |
| titulo | CharField(100) | Título de la notificación |
| mensaje | TextField | Contenido del mensaje |
| tipo | CharField(50) | Tipo de notificación |
| id_referencia | IntegerField | ID del objeto relacionado |
| tipo_referencia | CharField(50) | Tipo del objeto relacionado |
| leido | BooleanField | Si fue leída |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

---

## Documentación Swagger

Disponible en:
http://127.0.0.1:8081/swagger/
http://127.0.0.1:8081/redoc/

---

## Base de datos

- **Motor:** PostgreSQL
- **Base de datos:** `xchango_db`
- **Esquema:** `sistema`

Las tablas fueron creadas previamente con el proyecto Go (Beego). Django se conecta directamente a ellas sin necesidad de migraciones.