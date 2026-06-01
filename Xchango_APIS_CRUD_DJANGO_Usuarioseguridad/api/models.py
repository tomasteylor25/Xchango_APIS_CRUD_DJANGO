# modelos del API
from django.db import models


# Modelo tabla Usuario
class Usuario(models.Model):
    id_usuario         = models.AutoField(primary_key=True)
    correo             = models.CharField(max_length=100, unique=True)
    correo_verificado  = models.BooleanField(default=False)
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.correo

    class Meta:
        db_table = 'Usuario'


# Modelo tabla Credenciales
class Credenciales(models.Model):
    id_usuario         = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id_usuario'
    )
    contrasena_hash    = models.TextField()
    intentos_fallidos  = models.IntegerField(default=0)
    bloqueado          = models.BooleanField(default=False)
    ultimo_login       = models.DateTimeField(null=True, blank=True)
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Credenciales usuario {self.id_usuario_id}"

    class Meta:
        db_table = 'Credenciales'


# Modelo tabla Crear_contrasena
class CrearContrasena(models.Model):
    id_usuario           = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id_usuario'
    )
    contrasena           = models.TextField()
    confirmar_contrasena = models.TextField()
    activo               = models.BooleanField(default=True)
    fecha_creacion       = models.DateTimeField(auto_now_add=True)
    fecha_modificacion   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CrearContrasena usuario {self.id_usuario_id}"

    class Meta:
        db_table = 'Crear_contrasena'


# Modelo tabla HistorialContrasena
class HistorialContrasena(models.Model):
    id_historial       = models.AutoField(primary_key=True)
    id_usuario         = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario'
    )
    contrasena_hash    = models.TextField()
    fecha_cambio       = models.DateTimeField(auto_now_add=True)
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Historial {self.id_historial} - usuario {self.id_usuario_id}"

    class Meta:
        db_table = 'HistorialContrasena'


# Modelo tabla RecuperacionContrasena
class RecuperacionContrasena(models.Model):
    id_recuperacion    = models.AutoField(primary_key=True)
    id_usuario         = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario'
    )
    token              = models.TextField()
    codigo             = models.CharField(max_length=10, null=True, blank=True)
    usado              = models.BooleanField(default=False)
    fecha_expiracion   = models.DateTimeField()
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Recuperacion {self.id_recuperacion} - usuario {self.id_usuario_id}"

    class Meta:
        db_table = 'RecuperacionContrasena'


# Modelo tabla Sesion
class Sesion(models.Model):
    id_sesion          = models.AutoField(primary_key=True)
    id_usuario         = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario'
    )
    token_sesion       = models.TextField()
    ip_origen          = models.CharField(max_length=45, null=True, blank=True)
    user_agent         = models.TextField(null=True, blank=True)
    fecha_inicio       = models.DateTimeField(auto_now_add=True)
    fecha_expiracion   = models.DateTimeField()
    revocada           = models.BooleanField(default=False)
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sesion {self.id_sesion} - usuario {self.id_usuario_id}"

    class Meta:
        db_table = 'Sesion'


# Modelo tabla IntentoLogin
class IntentoLogin(models.Model):
    id_intento         = models.AutoField(primary_key=True)
    id_usuario         = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='id_usuario'
    )
    email_ingresado    = models.CharField(max_length=100, null=True, blank=True)
    exitoso            = models.BooleanField(default=False)
    motivo_fallo       = models.CharField(max_length=100, null=True, blank=True)
    ip_origen          = models.CharField(max_length=45, null=True, blank=True)
    fecha              = models.DateTimeField(auto_now_add=True)
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"IntentoLogin {self.id_intento}"

    class Meta:
        db_table = 'IntentoLogin'


# Modelo tabla Perfil
class Perfil(models.Model):
    id_perfil          = models.AutoField(primary_key=True)
    id_usuario         = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario'
    )
    nombre             = models.CharField(max_length=100)
    apellido           = models.CharField(max_length=100)
    telefono           = models.CharField(max_length=20, null=True, blank=True)
    whatsapp           = models.CharField(max_length=20)
    municipio          = models.CharField(max_length=50)
    barrio             = models.CharField(max_length=50, null=True, blank=True)
    genero             = models.CharField(max_length=20, null=True, blank=True)
    fecha_nacimiento   = models.DateField(null=True, blank=True)
    biografia          = models.TextField(null=True, blank=True)
    foto_perfil        = models.TextField(null=True, blank=True)
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'Perfil'
