from rest_framework import serializers

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


# Serializador para Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


# Serializador para Credenciales
class CredencialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credenciales
        fields = '__all__'


# Serializador para CrearContrasena
class CrearContrasenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrearContrasena
        fields = '__all__'


# Serializador para HistorialContrasena
class HistorialContrasenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialContrasena
        fields = '__all__'


# Serializador para RecuperacionContrasena
class RecuperacionContrasenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecuperacionContrasena
        fields = '__all__'


# Serializador para Sesion
class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields = '__all__'


# Serializador para IntentoLogin
class IntentoLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntentoLogin
        fields = '__all__'


# Serializador para Perfil
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'
