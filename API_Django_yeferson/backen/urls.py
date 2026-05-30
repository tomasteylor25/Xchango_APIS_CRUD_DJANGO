from rest_framework.routers import DefaultRouter

from .views import (
    NivelAccesoViewSet,
    PermisoViewSet,
    AdministradorViewSet,
    AdministradorPermisoViewSet,
    HistorialAdminViewSet,
    NotificacionViewSet,
)

#Registro de endpoints para cada api
router = DefaultRouter()
router.register(r'nivel_acceso',         NivelAccesoViewSet)
router.register(r'permiso',              PermisoViewSet)
router.register(r'administrador',        AdministradorViewSet)
router.register(r'administradorpermiso', AdministradorPermisoViewSet)
router.register(r'historialadmin',       HistorialAdminViewSet)
router.register(r'notificacion',         NotificacionViewSet)

urlpatterns = router.urls
