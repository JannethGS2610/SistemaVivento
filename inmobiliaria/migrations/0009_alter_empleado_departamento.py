# Generated by Django 3.2.3 on 2022-11-09 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0008_empleado_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inmobiliaria.departamento'),
        ),
    ]
