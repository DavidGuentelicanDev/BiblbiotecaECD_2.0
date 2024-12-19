# Generated by Django 5.1.4 on 2024-12-19 00:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0017_alter_detallereserva_estado_detalle_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallereserva',
            name='estado_detalle_reserva',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Reservado'), (2, 'Retirado'), (3, 'Devuelto'), (4, 'Atrasado'), (5, 'Perdido'), (6, 'Cancelado')], default=1, validators=[django.core.validators.MinValueValidator(1, message='Valor mínimo estado_detalle_reserva es 1'), django.core.validators.MaxValueValidator(6, message='Valor máximo estado_detalle_reserva es 6')]),
        ),
    ]
