# Generated by Django 3.2.3 on 2022-11-09 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0011_alter_empleado_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
