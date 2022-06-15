from django.db import models

class Vacantes(models.Model):
    titulo_vacante = models.CharField(max_length=100)
    descripcion_vacante = models.CharField(max_length=500)
    fecha_publicacion = models.DateTimeField("fecha de publicación")

    def __str__(self):
        return self.titulo_vacante

class DatosComplentariosVacantes(models.Model):
    vacantes = models.ForeignKey(Vacantes, on_delete=models.CASCADE)
    salario = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=30)

    def __str__(self):
        return self.salario, self.ciudad

class TipoDocumento(models.Model):
    nombre_documento = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_documento

class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre_ciudad

class TipoContrato(models.Model):
    nombre_tipo_contrato = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre_tipo_contrato

class Personas(models.Model):
    numero_documento = models.CharField(max_length=20)
    primer_nombre = models.CharField(max_length=70)
    otros_nombres = models.CharField(max_length=70, null=True, blank=True)
    primer_apellido = models.CharField(max_length=70)
    otros_apellidos = models.CharField(max_length=70, null=True, blank=True)
    correo_electronico = models.CharField(max_length=70)
    telefono = models.CharField(max_length=50)
    perfil = models.TextField(max_length=250)
    foto_persona = models.ImageField(null=True, blank=True)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_documento