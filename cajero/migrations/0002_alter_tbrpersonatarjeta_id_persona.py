# Generated by Django 4.2.5 on 2023-10-17 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0002_initial'),
        ('cajero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbrpersonatarjeta',
            name='id_persona',
            field=models.ForeignKey(blank=True, db_column='id_persona', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacion.persona'),
        ),
    ]
