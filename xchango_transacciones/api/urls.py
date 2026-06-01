from rest_framework.routers import DefaultRouter

from .views import (
    IntercambioViewSet,
    ContactoWhatsAppViewSet,
    CalificacionViewSet,
    ReporteViewSet,
)

router = DefaultRouter()
router.register(r'intercambio',        IntercambioViewSet,        basename='intercambio')
router.register(r'contacto_whatsapp',  ContactoWhatsAppViewSet,   basename='contacto_whatsapp')
router.register(r'calificacion',       CalificacionViewSet,       basename='calificacion')
router.register(r'reporte',            ReporteViewSet,            basename='reporte')

urlpatterns = router.urls
