# Generated by Django 4.2.5 on 2023-10-22 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0002_initial'),
        ('cajero', '0004_alter_tbrpersonatarjeta_id_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbstructure',
            name='id_especialista_complejo',
            field=models.ForeignKey(blank=True, db_column='id_especialista_complejo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='id_especialista_complejo_Structure', to='autenticacion.persona'),
        ),
        migrations.AlterField(
            model_name='tbstructure',
            name='id_sub_director',
            field=models.ForeignKey(blank=True, db_column='id_sub_director', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='id_sub_director_Structure', to='autenticacion.persona'),
        ),
        migrations.AlterField(
            model_name='tbstructure',
            name='id_tecnico_general',
            field=models.ForeignKey(blank=True, db_column='id_tecnico_general', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='id_tecnico_general_Structure', to='autenticacion.persona'),
        ),
    ]