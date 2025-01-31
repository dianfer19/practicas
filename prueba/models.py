from django.db import models

# Create your models here.
class Author(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50, verbose_name='Dirección',blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Autor'
        db_table = 'autores'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'