from django.db import models
from django.contrib.auth.models import AbstractUser


# MODELO DE CLASES ORM

#Editorial
class Editorial(models.Model):
    id_editorial     = models.SmallAutoField(primary_key=True)
    nombre_editorial = models.CharField(unique=True, max_length=40) #unique

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

#Autor
class Autor(models.Model):
    id_autor     = models.SmallAutoField(primary_key=True)
    nombre_autor = models.CharField(unique=True, max_length=50) #unique
    pseudonimo   = models.CharField(unique=True, max_length=50, blank=True, null=True) #unique, opcional

    def __str__(self):
        if (self.pseudonimo):
            return self.pseudonimo
        else:
            return self.nombre_autor

##############################################################################################################

#Autor por libro
class AutorPorLibro(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE) #FK de libro
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) #FK de autor

    def __str__(self):
        return f"{self.libro} - {self.autor}"

    class Meta:
        unique_together = ('libro', 'autor') #restriccion unica de ambos campos para emular pk dual con fk de tabla de interseccion

##############################################################################################################

#Usuario, usando clase abstracta para aprovechar todos los metodos prediseñados de django
class Usuario(AbstractUser):
    #diccionario de roles de usuario
    ROLES_USUARIO = [
        (1, 'Administrador'),
        (2, 'Bibliotecario'),
        (3, 'Recepción'),
        (4, 'Cliente')
    ]

    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    rut        = models.CharField(unique=True, max_length=12) #unique
    email      = models.EmailField(unique=True) #unique
    telefono   = models.CharField(max_length=15, blank=True, null=True)
    rol        = models.PositiveSmallIntegerField(choices=ROLES_USUARIO, default=4)

    def __str__(self):
        return self.username

##############################################################################################################
