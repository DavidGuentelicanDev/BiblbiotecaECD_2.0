# Generated by Django 5.1.4 on 2024-12-17 02:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='estado_libro',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ingresado'), (2, 'Disponible'), (3, 'Reservado'), (4, 'Prestado'), (5, 'Devuelto'), (6, 'Pendiente de devolución'), (7, 'Perdido'), (8, 'En reparación')], default=1),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('numero_reserva', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('cantidad_libros', models.PositiveSmallIntegerField(default=0)),
                ('fecha_confirmacion', models.DateField(blank=True, null=True)),
                ('fecha_compromiso', models.DateField(blank=True, null=True)),
                ('fecha_lista_retiro', models.DateField(blank=True, null=True)),
                ('fecha_max_retiro', models.DateField(blank=True, null=True)),
                ('fecha_retiro', models.DateField(blank=True, null=True)),
                ('fecha_cancelacion', models.DateField(blank=True, null=True)),
                ('estado_reserva', models.PositiveSmallIntegerField(choices=[(1, 'Provisoria'), (2, 'Confirmada'), (3, 'Lista para retiro'), (4, 'Retirada'), (5, 'Devuelta parcial'), (6, 'Devuelta completa'), (7, 'Atrasada'), (8, 'Cancelada')], default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
