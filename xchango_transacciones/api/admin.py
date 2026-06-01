from django.contrib import admin

from .models import (
    Intercambio,
    ContactoWhatsApp,
    Calificacion,
    Reporte,
)

admin.site.register(Intercambio)
admin.site.register(ContactoWhatsApp)
admin.site.register(Calificacion)
admin.site.register(Reporte)
