from django.db import models
from django.contrib.auth.models import AbstractUser


# MODELO DE CLASES ORM

#Editorial
class Editorial(models.Model):
    id_editorial     = models.SmallAutoField(primary_key=True)
    nombre_editorial = models.CharField(unique=True, max_length=40) #unique

    def __str__(self):
        return self.nombre_editorial

    class Meta:
        indexes = [models.Index(fields=['nombre_editorial'], name='Editorial_nombre_idx')] #index para nombre de editorial

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
        (1, 'Ingresado'), #recien ingresado al sistema
        (2, 'Disponible'), #disponible para reservas
        (3, 'Reservado'), #reservado
        (4, 'Prestado'), #retirado por el usuario
        (5, 'Devuelto'), #devuelto por el usuario
        (6, 'Pendiente de devolución'), #atrasado pero en proceso de recuperacion
        (7, 'Perdido'), #perdido permanentemente
        (8, 'En reparación') #en proceso de reparación o readquisicion
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

    class Meta:
        indexes = [
            models.Index(fields=['titulo'], name='Libro_titulo_idx'),
            models.Index(fields=['categoria'], name='Libro_categoria_idx'),
            models.Index(fields=['editorial'], name='Libro_editorial_idx'),
            models.Index(fields=['estado_libro'], name='Libro_estado_idx')
        ]

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

    class Meta:
        indexes = [
            models.Index(fields=['nombre_autor'], name='Autor_nombre_idx'),
            models.Index(fields=['pseudonimo'], name='Autor_pseudonimo_idx')
        ]

##############################################################################################################

#Autor por libro
class AutorPorLibro(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE) #FK de libro
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) #FK de autor

    def __str__(self):
        return f"{self.libro} - {self.autor}"

    class Meta:
        unique_together = ('libro', 'autor') #restriccion unica de ambos campos para emular pk dual con fk de tabla de interseccion
        #indices
        indexes = [
            models.Index(fields=['libro'], name='AutorPorLibro_libro_idx'),
            models.Index(fields=['autor'], name='AutorPorLibro_autor_idx')
        ]

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

#Reserva
class Reserva(models.Model):
    #diccionario estados de reserva
    ESTADOS_RESERVA = [
        (1, 'Provisoria'), #cuando se agrega el primer libro al carrito
        (2, 'Confirmada'), #cuando el usuario confirma la reserva
        (3, 'Lista para retiro'), #lista para ser retirada por el usuario
        (4, 'Retirada'), #retirada por el usuario
        (5, 'Devuelta parcial'), #devuelta parcial, faltaron libros
        (6, 'Devuelta completa'), #devuelta completa
        (7, 'Atrasada'), #no se ha devuelto nada
        (8, 'Cancelada') #cancelada por el usuario o por sistema
    ]

    numero_reserva     = models.BigAutoField(primary_key=True)
    usuario            = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    cantidad_libros    = models.PositiveSmallIntegerField(default=0)
    fecha_confirmacion = models.DateField(blank=True, null=True)
    fecha_compromiso   = models.DateField(blank=True, null=True)
    fecha_lista_retiro = models.DateField(blank=True, null=True)
    fecha_max_retiro   = models.DateField(blank=True, null=True)
    fecha_retiro       = models.DateField(blank=True, null=True)
    fecha_cancelacion  = models.DateField(blank=True, null=True)
    estado_reserva     = models.PositiveSmallIntegerField(choices=ESTADOS_RESERVA, default=1)

    def __str__(self):
        return self.numero_reserva

    class Meta:
        indexes = [
            models.Index(fields=['usuario'], name='Reserva_usuario_idx'),
            models.Index(fields=['fecha_compromiso'], name='Reserva_feccom_idx'),
            models.Index(fields=['fecha_max_retiro'], name='Reserva_fecmaxret_idx'),
            models.Index(fields=['estado_reserva'], name='Reserva_estado_idx')
        ]

##############################################################################################################

#Detalle reserva
class DetalleReserva(models.Model):
    #diccionario estados detalle reserva
    ESTADOS_DETALLE = [
        (1, 'Reservado'), #libro recien reservado
        (2, 'Prestado'), #libro ya en manos del usuario
        (3, 'Devuelto'), #libro devuelto
        (4, 'Atrasado'), #libro no devuelto
        (5, 'Perdido') #libro perdido
    ]

    id_detalle_reserva     = models.BigAutoField(primary_key=True)
    reserva                = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    libro                  = models.ForeignKey(Libro, on_delete=models.CASCADE)
    estado_detalle_reserva = models.PositiveSmallIntegerField(choices=ESTADOS_DETALLE, default=1)
    fecha_max_devolucion   = models.DateField(blank=True, null=True) #se calcula segun la logica de negocio
    fecha_devolucion       = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.reserva} - {self.libro}"

    class Meta:
        unique_together = ('reserva', 'libro') #no se puede repetir el libro en la misma reserva
        #indices
        indexes = [
            models.Index(fields=['reserva'], name='DetalleReserva_reserva_idx'),
            models.Index(fields=['libro'], name='DetalleReserva_libro_idx'),
            models.Index(fields=['estado_detalle_reserva'], name='DetalleReserva_estado_idx'),
            models.Index(fields=['fecha_max_devolucion'], name='DetalleReserva_fecmaxdev_idx')
        ]

##############################################################################################################

#Multa
class Multa(models.Model):
    usuario         = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    detalle_reserva = models.ForeignKey(DetalleReserva, on_delete=models.CASCADE)
    dias_atraso     = models.PositiveSmallIntegerField(default=1)
    monto_multa     = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.usuario} - {self.detalle_reserva}"

    class Meta:
        unique_together = ('usuario', 'detalle_reserva') #solo puede haber una multa por detallereserva
        #indices
        indexes = [
            models.Index(fields=['usuario'], name='Multa_usuario_idx'),
            models.Index(fields=['detalle_reserva'], name='Multa_detalle_idx'),
            models.Index(fields=['dias_atraso'], name='Multa_diasatraso_idx'),
            models.Index(fields=['monto_multa'], name='Multa_monto_idx')
        ]

##############################################################################################################
