from rest_framework.routers import DefaultRouter

from .views import (
    PublicacionViewSet,
    ImagenPublicacionViewSet,
    SubCategoriaViewSet,
    PublicacionCategoriaViewSet,
    BienFisicoViewSet,
    ServicioViewSet,
    BienDigitalViewSet,
    FavoritoViewSet,
)

router = DefaultRouter()
router.register(r'publicacion',          PublicacionViewSet,          basename='publicacion')
router.register(r'imagenpublicacion',    ImagenPublicacionViewSet,    basename='imagenpublicacion')
router.register(r'sub_categoria',        SubCategoriaViewSet,         basename='sub_categoria')
router.register(r'publicacioncategoria', PublicacionCategoriaViewSet, basename='publicacioncategoria')
router.register(r'bienfisico',           BienFisicoViewSet,           basename='bienfisico')
router.register(r'servicio',             ServicioViewSet,             basename='servicio')
router.register(r'biendigital',          BienDigitalViewSet,          basename='biendigital')
router.register(r'favorito',             FavoritoViewSet,             basename='favorito')

urlpatterns = router.urls
