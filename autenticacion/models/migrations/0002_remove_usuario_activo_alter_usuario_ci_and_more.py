# Generated by Django 4.2.5 on 2023-09-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='activo',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ci',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_completo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
