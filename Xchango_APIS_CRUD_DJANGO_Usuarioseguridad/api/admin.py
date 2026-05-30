from django.contrib import admin

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

admin.site.register(Usuario)
admin.site.register(Credenciales)
admin.site.register(CrearContrasena)
admin.site.register(HistorialContrasena)
admin.site.register(RecuperacionContrasena)
admin.site.register(Sesion)
admin.site.register(IntentoLogin)
admin.site.register(Perfil)
