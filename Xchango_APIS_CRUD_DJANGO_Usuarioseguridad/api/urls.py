from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    UsuarioViewSet,
    CredencialesViewSet,
    CrearContrasenaViewSet,
    HistorialContrasenaViewSet,
    RecuperacionContrasenaViewSet,
    SesionViewSet,
    IntentoLoginViewSet,
    PerfilViewSet,
)

router = DefaultRouter()

# Registro de endpoints del API
router.register(r'usuarios',                UsuarioViewSet)
router.register(r'credenciales',            CredencialesViewSet)
router.register(r'crear-contrasena',        CrearContrasenaViewSet)
router.register(r'historial-contrasena',    HistorialContrasenaViewSet)
router.register(r'recuperacion-contrasena', RecuperacionContrasenaViewSet)
router.register(r'sesiones',                SesionViewSet)
router.register(r'intentos-login',          IntentoLoginViewSet)
router.register(r'perfiles',                PerfilViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
