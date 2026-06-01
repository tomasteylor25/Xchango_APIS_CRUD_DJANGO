from django.shortcuts import render

from rest_framework import viewsets

from .models import (
    Intercambio,
    ContactoWhatsApp,
    Calificacion,
    Reporte,
)

from .serializers import (
    IntercambioSerializer,
    ContactoWhatsAppSerializer,
    CalificacionSerializer,
    ReporteSerializer,
)


# CRUD tabla Intercambio (GET, POST, PUT, DELETE)
class IntercambioViewSet(viewsets.ModelViewSet):
    queryset = Intercambio.objects.all()
    serializer_class = IntercambioSerializer


# CRUD tabla ContactoWhatsApp (GET, POST, PUT, DELETE)
class ContactoWhatsAppViewSet(viewsets.ModelViewSet):
    queryset = ContactoWhatsApp.objects.all()
    serializer_class = ContactoWhatsAppSerializer


# CRUD tabla Calificacion (GET, POST, PUT, DELETE)
class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer


# CRUD tabla Reporte (GET, POST, PUT, DELETE)
class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
