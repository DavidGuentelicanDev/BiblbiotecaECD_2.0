from django.db import models


# MODELO DE CLASES ORM

#Editorial
class Editorial(models.Model):
    id_editorial     = models.SmallAutoField(primary_key=True)
    nombre_editorial = models.CharField(unique=True, max_length=40) #unique, para evitar que se repita

    def __str__(self):
        return self.nombre_editorial

##############################################################################################################

#Libro
class Libro(models.Model):
    #diccionario categorias
    CATEGORIAS_LIBRO = [
        (1, 'Novela'),
        (2, 'Poesía'),
        (3, 'Cuentos'),
        (4, 'Filosofía'),
        (5, 'Historia')
    ]

    #diccionario estados
    ESTADOS_LIBRO = [
        (1, 'Ingresado'),
        (2, 'Disponible'),
        (3, 'Reservado'),
        (4, 'Prestado'),
        (5, 'Devuelto'),
        (6, 'Pendiente'),
        (7, 'Perdido'),
        (8, 'En reparación')
    ]

    codigo_libro = models.PositiveSmallIntegerField(primary_key=True) #manual
    titulo       = models.CharField(max_length=50)
    subtitulo    = models.CharField(max_length=50, blank=True, null=True) #opcional
    resena       = models.TextField(blank=True, null=True) #opcional
    categoria    = models.PositiveSmallIntegerField(choices=CATEGORIAS_LIBRO) #diccionario CATEGORIAS_LIBRO
    editorial    = models.ForeignKey(Editorial, on_delete=models.CASCADE) #FK de editorial
    portada      = models.ImageField(upload_to='media/', blank=True, null=True) #se carga en carpeta media, opcional
    estado_libro = models.PositiveSmallIntegerField(choices=ESTADOS_LIBRO, default=1) #diccionario ESTADOS_LIBRO, por defecto 1

    def __str__(self):
        if (self.subtitulo):
            return f"{self.titulo}. {self.subtitulo}"
        else:
            return self.titulo

##############################################################################################################
