from rest_framework import serializers

from .models import (
    NivelAcceso,
    Permiso,
    Administrador,
    AdministradorPermiso,
    HistorialAdmin,
    Notificacion,
)


# Serializer para nivel_acceso
class NivelAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelAcceso
        fields = '__all__'


# Serializer para permiso
class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'


# Serializer para administrador
class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'


# Serializer para administradorpermiso
class AdministradorPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministradorPermiso
        fields = '__all__'


# Serializer para historialadmin
class HistorialAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialAdmin
        fields = '__all__'


# Serializer para notificacion
class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'
