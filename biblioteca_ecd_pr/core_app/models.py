from django.db import models


# MODELO DE CLASES ORM

#Editorial
class Editorial(models.Model):
    id_editorial = models.SmallAutoField(primary_key=True)
    nombre_editorial = models.CharField(unique=True, max_length=40) #unique, para evitar que se repita

    def __str__(self):
        return self.nombre_editorial
