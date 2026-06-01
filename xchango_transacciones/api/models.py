from django.db import models


# Modelo tabla Intercambio
class Intercambio(models.Model):
    id_intercambio = models.AutoField(primary_key=True)
    id_publicacion = models.IntegerField()
    id_usuario_interesado = models.IntegerField()
    estado = models.CharField(max_length=20, default='iniciado')
    mensaje_inicial = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Intercambio {self.id_intercambio}'

    class Meta:
        db_table = '"Transacciones_comunicacion"."Intercambio"'


# Modelo tabla ContactoWhatsApp
class ContactoWhatsApp(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    id_publicacion = models.IntegerField()
    id_usuario_interesado = models.IntegerField()
    id_usuario_propietario = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'ContactoWhatsApp {self.id_contacto}'

    class Meta:
        db_table = '"Transacciones_comunicacion"."ContactoWhatsApp"'


# Modelo tabla Calificacion
class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    id_intercambio = models.ForeignKey(
        Intercambio,
        on_delete=models.CASCADE,
        db_column='id_intercambio'
    )
    id_usuario_califica = models.IntegerField()
    id_usuario_calificado = models.IntegerField()
    puntuacion = models.IntegerField()
    comentario = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Calificacion {self.id_calificacion}'

    class Meta:
        db_table = '"Transacciones_comunicacion"."Calificacion"'


# Modelo tabla Reporte
class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_publicacion = models.IntegerField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, default='pendiente')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Reporte {self.id_reporte}'

    class Meta:
        db_table = '"Transacciones_comunicacion"."Reporte"'
