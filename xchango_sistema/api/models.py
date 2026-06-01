from django.db import models


# Modelo tabla nivel_acceso
class NivelAcceso(models.Model):
    id_nivelacceso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'nivel_acceso'


# Modelo tabla permiso
class Permiso(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'permiso'


# Modelo tabla administrador
class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField(unique=True)
    id_nivelacceso = models.ForeignKey(
        NivelAcceso,
        on_delete=models.PROTECT,
        db_column='id_nivelacceso'
    )
    activo = models.BooleanField(default=True)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Administrador {self.id_admin}'

    class Meta:
        db_table = 'administrador'


# Modelo tabla administradorpermiso
class AdministradorPermiso(models.Model):
    id = models.AutoField(primary_key=True)
    id_admin = models.ForeignKey(
        Administrador,
        on_delete=models.CASCADE,
        db_column='id_admin'
    )
    id_permiso = models.ForeignKey(
        Permiso,
        on_delete=models.CASCADE,
        db_column='id_permiso'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'AdminPermiso {self.id}'

    class Meta:
        db_table = 'administradorpermiso'


# Modelo tabla historialadmin
class HistorialAdmin(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_admin = models.ForeignKey(
        Administrador,
        on_delete=models.CASCADE,
        db_column='id_admin'
    )
    accion = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    tipo_objeto = models.CharField(max_length=50, null=True, blank=True)
    id_objeto = models.IntegerField(null=True, blank=True)
    fecha_accion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.accion} - Admin {self.id_admin_id}'

    class Meta:
        db_table = 'historialadmin'


# Modelo tabla notificacion
class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    tipo = models.CharField(max_length=50)
    id_referencia = models.IntegerField(null=True, blank=True)
    tipo_referencia = models.CharField(max_length=50, null=True, blank=True)
    leido = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'notificacion'
