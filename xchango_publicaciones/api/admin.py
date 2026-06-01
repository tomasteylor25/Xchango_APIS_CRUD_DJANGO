from django.contrib import admin

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

admin.site.register(Publicacion)
admin.site.register(ImagenPublicacion)
admin.site.register(SubCategoria)
admin.site.register(PublicacionCategoria)
admin.site.register(BienFisico)
admin.site.register(Servicio)
admin.site.register(BienDigital)
admin.site.register(Favorito)
