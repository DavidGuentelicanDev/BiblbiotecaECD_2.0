# Generated by Django 5.1.4 on 2024-12-17 16:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0014_alter_detallereserva_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estado_reserva',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Provisoria'), (2, 'Confirmada'), (3, 'Lista para retiro'), (4, 'Retirada'), (5, 'Devuelta parcial'), (6, 'Devuelta completa'), (7, 'Atrasada'), (8, 'Cancelada')], default=1, validators=[django.core.validators.MinValueValidator(1, message='Valor mínimo de estado_reserva es 1'), django.core.validators.MaxValueValidator(8, message='Valor máximo de estado_reserva es 8')]),
        ),
    ]