# Generated by Django 3.2.3 on 2022-10-19 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='image',
            new_name='imagen',
        ),
    ]
