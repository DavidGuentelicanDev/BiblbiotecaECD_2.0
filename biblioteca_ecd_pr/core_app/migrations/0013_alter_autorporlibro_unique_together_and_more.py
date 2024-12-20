# Generated by Django 5.1.4 on 2024-12-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0012_remove_autor_autor_nombre_idx_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='autorporlibro',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='autorporlibro',
            constraint=models.UniqueConstraint(fields=('libro', 'autor'), name='AutorPorLibro_libroautor_un'),
        ),
    ]
