from django.shortcuts import render

from rest_framework import viewsets

from .models import (
    NivelAcceso,
    Permiso,
    Administrador,
    AdministradorPermiso,
    HistorialAdmin,
    Notificacion,
)

from .serializers import (
    NivelAccesoSerializer,
    PermisoSerializer,
    AdministradorSerializer,
    AdministradorPermisoSerializer,
    HistorialAdminSerializer,
    NotificacionSerializer,
)


# CRUD tabla nivel_acceso (GET, POST, PUT, DELETE)
class NivelAccesoViewSet(viewsets.ModelViewSet):
    queryset = NivelAcceso.objects.all()
    serializer_class = NivelAccesoSerializer


# CRUD tabla permiso (GET, POST, PUT, DELETE)
class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer


# CRUD tabla administrador (GET, POST, PUT, DELETE)
class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer


# CRUD tabla administradorpermiso (GET, POST, PUT, DELETE)
class AdministradorPermisoViewSet(viewsets.ModelViewSet):
    queryset = AdministradorPermiso.objects.all()
    serializer_class = AdministradorPermisoSerializer


# CRUD tabla historialadmin (GET, POST, PUT, DELETE)
class HistorialAdminViewSet(viewsets.ModelViewSet):
    queryset = HistorialAdmin.objects.all()
    serializer_class = HistorialAdminSerializer


# CRUD tabla notificacion (GET, POST, PUT, DELETE)
class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer


# Create your views here.
