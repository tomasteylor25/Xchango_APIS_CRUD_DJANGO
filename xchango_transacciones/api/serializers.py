from rest_framework import serializers

from .models import (
    Intercambio,
    ContactoWhatsApp,
    Calificacion,
    Reporte,
)


# Serializer para Intercambio
class IntercambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intercambio
        fields = '__all__'


# Serializer para ContactoWhatsApp
class ContactoWhatsAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactoWhatsApp
        fields = '__all__'


# Serializer para Calificacion
class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'


# Serializer para Reporte
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'
