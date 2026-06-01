# Xchango API — Módulo Publicaciones

API REST CRUD para el módulo de publicaciones del sistema **Xchango**, desarrollada en **Django 6 + Django REST Framework + PostgreSQL**.

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

---

## Estructura del proyecto

```
xchango_publicaciones/
├── .env                    ← Variables de entorno (NO subir al repo)
├── .gitignore
├── manage.py
├── run.py                  ← Shortcut para correr el servidor
├── backen/
│   ├── __init__.py
│   ├── settings.py         ← Configuración del proyecto
│   ├── urls.py             ← Rutas raíz + Swagger
│   ├── asgi.py
│   └── wsgi.py
└── api/
    ├── __init__.py
    ├── apps.py
    ├── models.py           ← 8 modelos del schema 'Publicaciones'
    ├── serializers.py      ← Serializers de cada modelo
    ├── views.py            ← ViewSets CRUD
    ├── urls.py             ← Router con los 8 recursos
    ├── admin.py
    ├── tests.py
    └── migrations/
        └── __init__.py
```

---

## Instalación

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual (Windows)
venv\Scripts\activate.bat

# 3. Instalar dependencias
pip install django djangorestframework psycopg2-binary drf-yasg python-decouple setuptools
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
```
http://127.0.0.1:8082/
```

> **Importante:** NO ejecutes `makemigrations` ni `migrate`. Las tablas ya existen en PostgreSQL. Django simplemente las usa.

---

## Endpoints

Todos los endpoints tienen el prefijo `/publicaciones/`.

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/publicaciones/{recurso}/` | Listar todos los registros |
| `POST` | `/publicaciones/{recurso}/` | Crear un nuevo registro |
| `GET` | `/publicaciones/{recurso}/{id}/` | Obtener un registro por ID |
| `PUT` | `/publicaciones/{recurso}/{id}/` | Actualizar un registro completo |
| `PATCH` | `/publicaciones/{recurso}/{id}/` | Actualizar un registro parcialmente |
| `DELETE` | `/publicaciones/{recurso}/{id}/` | Eliminar un registro |

---

## Recursos disponibles

| Modelo | Ruta | Tabla en DB |
|---|---|---|
| Publicacion | `/publicaciones/publicacion/` | `publicacion` |
| ImagenPublicacion | `/publicaciones/imagenpublicacion/` | `imagenpublicacion` |
| SubCategoria | `/publicaciones/sub_categoria/` | `sub_categoria` |
| PublicacionCategoria | `/publicaciones/publicacioncategoria/` | `publicacioncategoria` |
| BienFisico | `/publicaciones/bienfisico/` | `bienfisico` |
| Servicio | `/publicaciones/servicio/` | `servicio` |
| BienDigital | `/publicaciones/biendigital/` | `biendigital` |
| Favorito | `/publicaciones/favorito/` | `favorito` |

---

## Modelos

### Publicacion
| Campo | Tipo | Descripción |
|---|---|---|
| id_publicacion | AutoField | PK |
| id_usuario | IntegerField | ID del usuario propietario |
| estadopublicacion | BooleanField | Estado de la publicación |
| titulo | CharField(150) | Título |
| descripcion | TextField | Descripción |
| tipo | CharField(20) | Tipo de publicación |
| visibilidad | CharField(20) | Visibilidad (publica/privada) |
| departamento | CharField(50) | Departamento |
| municipio | CharField(50) | Municipio |
| barrio | CharField(50) | Barrio opcional |
| disponible_para_trueque | BooleanField | Disponible para trueque |
| cantidad_disponible | IntegerField | Cantidad disponible |
| prioridad | IntegerField | Prioridad en listados |
| mensaje_contacto | TextField | Mensaje de contacto opcional |
| vistas | IntegerField | Número de vistas |
| favoritos | IntegerField | Número de favoritos |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### ImagenPublicacion
| Campo | Tipo | Descripción |
|---|---|---|
| id_imagen | AutoField | PK |
| id_publicacion | ForeignKey | Publicación asociada |
| url | TextField | URL de la imagen |
| tipo | CharField(20) | Tipo de imagen |
| orden | IntegerField | Orden de visualización |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### SubCategoria
| Campo | Tipo | Descripción |
|---|---|---|
| id_categoria | AutoField | PK |
| electronico | CharField(255) | Subcategoría electrónico |
| vehiculos | CharField(255) | Subcategoría vehículos |
| ropa | CharField(255) | Subcategoría ropa |
| libros | CharField(255) | Subcategoría libros |
| muebles | CharField(255) | Subcategoría muebles |
| juguetes | CharField(255) | Subcategoría juguetes |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### PublicacionCategoria
| Campo | Tipo | Descripción |
|---|---|---|
| id | AutoField | PK |
| id_publicacion | ForeignKey | Publicación asociada |
| id_categoria | ForeignKey | Subcategoría asociada |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### BienFisico
| Campo | Tipo | Descripción |
|---|---|---|
| id_bien | AutoField | PK |
| id_publicacion | OneToOneField | Publicación asociada |
| estado_producto | CharField(50) | Estado del producto |
| marca | CharField(100) | Marca |
| modelo | CharField(100) | Modelo |
| color | CharField(50) | Color |
| peso | DecimalField | Peso en kg |
| dimensiones | CharField(100) | Dimensiones |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### Servicio
| Campo | Tipo | Descripción |
|---|---|---|
| id_servicio | AutoField | PK |
| id_publicacion | OneToOneField | Publicación asociada |
| duracion | CharField(50) | Duración del servicio |
| modalidad | CharField(50) | Modalidad (presencial/virtual) |
| disponibilidad | TextField | Disponibilidad horaria |
| requisitos | TextField | Requisitos opcionales |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### BienDigital
| Campo | Tipo | Descripción |
|---|---|---|
| id_bien_digital | AutoField | PK |
| id_publicacion | OneToOneField | Publicación asociada |
| tipo_archivo | CharField(50) | Tipo de archivo |
| tamano_mb | DecimalField | Tamaño en MB |
| licencia | CharField(100) | Tipo de licencia |
| acceso_inmediato | BooleanField | Acceso inmediato tras trueque |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

### Favorito
| Campo | Tipo | Descripción |
|---|---|---|
| id_favorito | AutoField | PK |
| id_usuario | IntegerField | ID del usuario |
| id_publicacion | ForeignKey | Publicación marcada como favorita |
| activo | BooleanField | Estado |
| fecha_creacion | DateTimeField | Fecha de creación |
| fecha_modificacion | DateTimeField | Última modificación |

---

## Documentación Swagger

Disponible en:

```
http://127.0.0.1:8082/swagger/
http://127.0.0.1:8082/redoc/
```

---

## Base de datos

- **Motor:** PostgreSQL
- **Base de datos:** `xchango_db`
- **Schema:** `Publicaciones`

Las tablas fueron creadas previamente con el proyecto Go (Beego). Django se conecta directamente a ellas sin necesidad de migraciones.
