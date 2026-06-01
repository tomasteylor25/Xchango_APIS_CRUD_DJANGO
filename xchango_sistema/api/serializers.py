from rest_framework import serializers

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


# Serializer para publicacion
class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'


# Serializer para imagenpublicacion
class ImagenPublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenPublicacion
        fields = '__all__'


# Serializer para sub_categoria
class SubCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoria
        fields = '__all__'


# Serializer para publicacioncategoria
class PublicacionCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicacionCategoria
        fields = '__all__'


# Serializer para bienfisico
class BienFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BienFisico
        fields = '__all__'


# Serializer para servicio
class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'


# Serializer para biendigital
class BienDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BienDigital
        fields = '__all__'


# Serializer para favorito
class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'
