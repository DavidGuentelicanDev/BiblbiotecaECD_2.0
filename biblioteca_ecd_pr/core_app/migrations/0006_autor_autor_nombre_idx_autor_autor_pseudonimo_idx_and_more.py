# Generated by Django 5.1.4 on 2024-12-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0005_editorial_editorial_nombre_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='autor',
            index=models.Index(fields=['nombre_autor'], name='Autor_nombre_idx'),
        ),
        migrations.AddIndex(
            model_name='autor',
            index=models.Index(fields=['pseudonimo'], name='Autor_pseudonimo_idx'),
        ),
        migrations.AddIndex(
            model_name='libro',
            index=models.Index(fields=['titulo'], name='Libro_titulo_idx'),
        ),
        migrations.AddIndex(
            model_name='libro',
            index=models.Index(fields=['categoria'], name='Libro_categoria_idx'),
        ),
        migrations.AddIndex(
            model_name='libro',
            index=models.Index(fields=['editorial'], name='Libro_editorial_idx'),
        ),
        migrations.AddIndex(
            model_name='libro',
            index=models.Index(fields=['estado_libro'], name='Libro_estado_idx'),
        ),
    ]
