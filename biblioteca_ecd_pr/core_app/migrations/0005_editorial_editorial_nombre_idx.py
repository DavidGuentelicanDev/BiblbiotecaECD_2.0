# Generated by Django 5.1.4 on 2024-12-17 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0004_alter_detallereserva_unique_together_multa'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='editorial',
            index=models.Index(fields=['nombre_editorial'], name='Editorial_nombre_idx'),
        ),
    ]
