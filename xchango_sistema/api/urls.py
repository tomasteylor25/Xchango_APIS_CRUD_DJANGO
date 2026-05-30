from rest_framework.routers import DefaultRouter

from .views import (
    NivelAccesoViewSet,
    PermisoViewSet,
    AdministradorViewSet,
    AdministradorPermisoViewSet,
    HistorialAdminViewSet,
    NotificacionViewSet,
)

router = DefaultRouter()
router.register(r'nivel_acceso',         NivelAccesoViewSet,         basename='nivel_acceso')
router.register(r'permiso',              PermisoViewSet,             basename='permiso')
router.register(r'administrador',        AdministradorViewSet,       basename='administrador')
router.register(r'administradorpermiso', AdministradorPermisoViewSet, basename='administradorpermiso')
router.register(r'historialadmin',       HistorialAdminViewSet,      basename='historialadmin')
router.register(r'notificacion',         NotificacionViewSet,        basename='notificacion')

urlpatterns = router.urls
