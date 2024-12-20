# Generated by Django 5.1.4 on 2024-12-17 03:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_alter_libro_estado_libro_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleReserva',
            fields=[
                ('id_detalle_reserva', models.BigAutoField(primary_key=True, serialize=False)),
                ('estado_detalle_reserva', models.PositiveSmallIntegerField(choices=[(1, 'Reservado'), (2, 'Prestado'), (3, 'Devuelto'), (4, 'Atrasado'), (5, 'Perdido')], default=1)),
                ('fecha_max_devolucion', models.DateField(blank=True, null=True)),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.libro')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.reserva')),
            ],
        ),
    ]
