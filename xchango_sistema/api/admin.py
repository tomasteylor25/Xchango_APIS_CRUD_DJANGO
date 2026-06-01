from django.contrib import admin

from .models import (
    NivelAcceso,
    Permiso,
    Administrador,
    AdministradorPermiso,
    HistorialAdmin,
    Notificacion,
)

admin.site.register(NivelAcceso)
admin.site.register(Permiso)
admin.site.register(Administrador)
admin.site.register(AdministradorPermiso)
admin.site.register(HistorialAdmin)
admin.site.register(Notificacion)
