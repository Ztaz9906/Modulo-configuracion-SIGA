# Generated by Django 4.2.5 on 2023-10-17 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0002_initial'),
        ('cajero', '0003_alter_tbrpersonatarjeta_id_tarjeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbrpersonatarjeta',
            name='id_persona',
            field=models.ForeignKey(blank=True, db_column='id_persona', null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacion.persona'),
        ),
    ]
