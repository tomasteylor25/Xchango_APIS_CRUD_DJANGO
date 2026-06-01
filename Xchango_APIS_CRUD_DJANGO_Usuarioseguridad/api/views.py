from rest_framework import viewsets

from .models import (
    Usuario,
    Credenciales,
    CrearContrasena,
    HistorialContrasena,
    RecuperacionContrasena,
    Sesion,
    IntentoLogin,
    Perfil,
)

from .serializers import (
    UsuarioSerializer,
    CredencialesSerializer,
    CrearContrasenaSerializer,
    HistorialContrasenaSerializer,
    RecuperacionContrasenaSerializer,
    SesionSerializer,
    IntentoLoginSerializer,
    PerfilSerializer,
)


# CRUD tabla Usuario (GET, POST, PUT, DELETE)
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# CRUD tabla Credenciales (GET, POST, PUT, DELETE)
class CredencialesViewSet(viewsets.ModelViewSet):
    queryset = Credenciales.objects.all()
    serializer_class = CredencialesSerializer


# CRUD tabla CrearContrasena (GET, POST, PUT, DELETE)
class CrearContrasenaViewSet(viewsets.ModelViewSet):
    queryset = CrearContrasena.objects.all()
    serializer_class = CrearContrasenaSerializer


# CRUD tabla HistorialContrasena (GET, POST, PUT, DELETE)
class HistorialContrasenaViewSet(viewsets.ModelViewSet):
    queryset = HistorialContrasena.objects.all()
    serializer_class = HistorialContrasenaSerializer


# CRUD tabla RecuperacionContrasena (GET, POST, PUT, DELETE)
class RecuperacionContrasenaViewSet(viewsets.ModelViewSet):
    queryset = RecuperacionContrasena.objects.all()
    serializer_class = RecuperacionContrasenaSerializer


# CRUD tabla Sesion (GET, POST, PUT, DELETE)
class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer


# CRUD tabla IntentoLogin (GET, POST, PUT, DELETE)
class IntentoLoginViewSet(viewsets.ModelViewSet):
    queryset = IntentoLogin.objects.all()
    serializer_class = IntentoLoginSerializer


# CRUD tabla Perfil (GET, POST, PUT, DELETE)
class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
