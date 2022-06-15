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
