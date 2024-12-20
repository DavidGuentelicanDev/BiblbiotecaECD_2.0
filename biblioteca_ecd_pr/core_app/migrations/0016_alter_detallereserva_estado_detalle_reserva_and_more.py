# Generated by Django 5.1.4 on 2024-12-17 16:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0015_alter_reserva_estado_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallereserva',
            name='estado_detalle_reserva',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Reservado'), (2, 'Prestado'), (3, 'Devuelto'), (4, 'Atrasado'), (5, 'Perdido')], default=1, validators=[django.core.validators.MinValueValidator(1, message='Valor mínimo estado_detalle_reserva es 1'), django.core.validators.MaxValueValidator(5, message='Valor máximo estado_detalle_reserva es 5')]),
        ),
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Novela'), (2, 'Poesía'), (3, 'Cuentos'), (4, 'Filosofía'), (5, 'Historia')], validators=[django.core.validators.MinValueValidator(1, message='Valor mínimo categoria es 1'), django.core.validators.MaxValueValidator(5, message='Valor máximo categoria es 5')]),
        ),
        migrations.AlterField(
            model_name='libro',
            name='estado_libro',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ingresado'), (2, 'Disponible'), (3, 'Reservado'), (4, 'Prestado'), (5, 'Devuelto'), (6, 'Pendiente de devolución'), (7, 'Perdido'), (8, 'En reparación')], default=1, validators=[django.core.validators.MinValueValidator(1, message='Valor mínimo estado_libro es 1'), django.core.validators.MaxValueValidator(8, message='Valor máximo estado_libro es 8')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Administrador'), (2, 'Bibliotecario'), (3, 'Recepción'), (4, 'Cliente')], default=4, validators=[django.core.validators.MinValueValidator(1, message='Valor mínimo rol es 1'), django.core.validators.MaxValueValidator(4, message='Valor máximo rol es 4')]),
        ),
    ]
