from django.db import models


# Create your models here.
class Barrio(models.Model):
    nombre_barrio = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)

    def __str__(self):
        return "%s %s" % (self.nombre_barrio,
                          self.siglas
                          )


class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    cedula = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.nombres,
                                self.apellidos,
                                self.cedula,
                                self.correo
                                )


class Casa(models.Model):
    prop_casa = models.ForeignKey(Persona, on_delete=models.CASCADE,
                               related_name="propietario_casa")
    direccion_casa = models.CharField(max_length=100)
    valor_casa = models.IntegerField()
    color = models.CharField(max_length=20)
    cuartos_casa = models.IntegerField()
    pisos = models.IntegerField()
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
                               related_name="ubicacion_casa")

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.prop_casa,
                                         self.direccion_casa,
                                         self.valor_casa,
                                         self.color,
                                         self.cuartos_casa,
                                         self.pisos,
                                         self.barrio
                                         )


class Departamento(models.Model):
    prop_dept = models.ForeignKey(Persona, on_delete=models.CASCADE,
                                  related_name="propietario_dept")
    direccion_dept = models.CharField(max_length=100)
    valor_dept = models.IntegerField()
    cuartos_dept = models.IntegerField()
    mensualidad = models.IntegerField()
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
                               related_name="ubicacion_dept")

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.prop_dept,
                                      self.direccion_dept,
                                      self.valor_dept,
                                      self.cuartos_dept,
                                      self.mensualidad,
                                      self.barrio
                                      )
