from django.db import models


# Modelo tabla publicacion
class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    estadopublicacion = models.BooleanField(default=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20)
    visibilidad = models.CharField(max_length=20, default='publica')
    departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    barrio = models.CharField(max_length=50, null=True, blank=True)
    disponible_para_trueque = models.BooleanField(default=True)
    cantidad_disponible = models.IntegerField(default=1)
    prioridad = models.IntegerField(default=0)
    mensaje_contacto = models.TextField(null=True, blank=True)
    vistas = models.IntegerField(default=0)
    favoritos = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'publicacion'


# Modelo tabla imagenpublicacion
class ImagenPublicacion(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    id_publicacion = models.ForeignKey(
        Publicacion,
        on_delete=models.CASCADE,
        db_column='id_publicacion'
    )
    url = models.TextField()
    tipo = models.CharField(max_length=20, null=True, blank=True)
    orden = models.IntegerField(default=1)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Imagen {self.id_imagen}'

    class Meta:
        db_table = 'imagenpublicacion'


# Modelo tabla sub_categoria
class SubCategoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    electronico = models.CharField(max_length=255, null=True, blank=True)
    vehiculos = models.CharField(max_length=255, null=True, blank=True)
    ropa = models.CharField(max_length=255, null=True, blank=True)
    libros = models.CharField(max_length=255, null=True, blank=True)
    muebles = models.CharField(max_length=255, null=True, blank=True)
    juguetes = models.CharField(max_length=255, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'SubCategoria {self.id_categoria}'

    class Meta:
        db_table = 'sub_categoria'


# Modelo tabla publicacioncategoria
class PublicacionCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    id_publicacion = models.ForeignKey(
        Publicacion,
        on_delete=models.CASCADE,
        db_column='id_publicacion'
    )
    id_categoria = models.ForeignKey(
        SubCategoria,
        on_delete=models.CASCADE,
        db_column='id_categoria'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'PublicacionCategoria {self.id}'

    class Meta:
        db_table = 'publicacioncategoria'


# Modelo tabla bienFisico
class BienFisico(models.Model):
    id_bien = models.AutoField(primary_key=True)
    id_publicacion = models.OneToOneField(
        Publicacion,
        on_delete=models.CASCADE,
        db_column='id_publicacion'
    )
    estado_producto = models.CharField(max_length=50, null=True, blank=True)
    marca = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dimensiones = models.CharField(max_length=100, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'BienFisico {self.id_bien}'

    class Meta:
        db_table = 'bienfisico'


# Modelo tabla servicio
class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    id_publicacion = models.OneToOneField(
        Publicacion,
        on_delete=models.CASCADE,
        db_column='id_publicacion'
    )
    duracion = models.CharField(max_length=50, null=True, blank=True)
    modalidad = models.CharField(max_length=50, null=True, blank=True)
    disponibilidad = models.TextField(null=True, blank=True)
    requisitos = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Servicio {self.id_servicio}'

    class Meta:
        db_table = 'servicio'


# Modelo tabla biendigital
class BienDigital(models.Model):
    id_bien_digital = models.AutoField(primary_key=True)
    id_publicacion = models.OneToOneField(
        Publicacion,
        on_delete=models.CASCADE,
        db_column='id_publicacion'
    )
    tipo_archivo = models.CharField(max_length=50, null=True, blank=True)
    tamano_mb = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    licencia = models.CharField(max_length=100, null=True, blank=True)
    acceso_inmediato = models.BooleanField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'BienDigital {self.id_bien_digital}'

    class Meta:
        db_table = 'biendigital'


# Modelo tabla favorito
class Favorito(models.Model):
    id_favorito = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_publicacion = models.ForeignKey(
        Publicacion,
        on_delete=models.CASCADE,
        db_column='id_publicacion'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Favorito {self.id_favorito}'

    class Meta:
        db_table = 'favorito'
