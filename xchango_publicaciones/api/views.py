from django.shortcuts import render

from rest_framework import viewsets

from .models import (
    Publicacion,
    ImagenPublicacion,
    SubCategoria,
    PublicacionCategoria,
    BienFisico,
    Servicio,
    BienDigital,
    Favorito,
)

from .serializers import (
    PublicacionSerializer,
    ImagenPublicacionSerializer,
    SubCategoriaSerializer,
    PublicacionCategoriaSerializer,
    BienFisicoSerializer,
    ServicioSerializer,
    BienDigitalSerializer,
    FavoritoSerializer,
)


# CRUD tabla publicacion (GET, POST, PUT, DELETE)
class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer


# CRUD tabla imagenpublicacion (GET, POST, PUT, DELETE)
class ImagenPublicacionViewSet(viewsets.ModelViewSet):
    queryset = ImagenPublicacion.objects.all()
    serializer_class = ImagenPublicacionSerializer


# CRUD tabla sub_categoria (GET, POST, PUT, DELETE)
class SubCategoriaViewSet(viewsets.ModelViewSet):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer


# CRUD tabla publicacioncategoria (GET, POST, PUT, DELETE)
class PublicacionCategoriaViewSet(viewsets.ModelViewSet):
    queryset = PublicacionCategoria.objects.all()
    serializer_class = PublicacionCategoriaSerializer


# CRUD tabla bienfisico (GET, POST, PUT, DELETE)
class BienFisicoViewSet(viewsets.ModelViewSet):
    queryset = BienFisico.objects.all()
    serializer_class = BienFisicoSerializer


# CRUD tabla servicio (GET, POST, PUT, DELETE)
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


# CRUD tabla biendigital (GET, POST, PUT, DELETE)
class BienDigitalViewSet(viewsets.ModelViewSet):
    queryset = BienDigital.objects.all()
    serializer_class = BienDigitalSerializer


# CRUD tabla favorito (GET, POST, PUT, DELETE)
class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
