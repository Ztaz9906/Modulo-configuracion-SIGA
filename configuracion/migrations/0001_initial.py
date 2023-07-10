# Generated by Django 4.1.3 on 2023-07-04 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TbDconfiguracionPersona',
            fields=[
                ('id_configuracion_persona', models.AutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_registro', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tb_dconfiguracion_persona',
            },
        ),
        migrations.CreateModel(
            name='TbDvaloresConfiguracionPersona',
            fields=[
                ('id_calores_configuracion_persona', models.AutoField(primary_key=True, serialize=False)),
                ('id_categoria', models.ForeignKey(blank=True, db_column='id_categoria', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.tbncategoria')),
                ('id_categoria_residente', models.ForeignKey(blank=True, db_column='id_categoria_residente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.tbncategoriaresidente')),
                ('id_configuracion_persona', models.ForeignKey(blank=True, db_column='id_configuracion_persona', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='configuracion.tbdconfiguracionpersona')),
                ('id_estructura', models.ForeignKey(blank=True, db_column='id_estructura', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.tbnestructura')),
                ('id_tipo_curso', models.ForeignKey(blank=True, db_column='id_tipo_curso', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.tbntipocurso')),
            ],
            options={
                'db_table': 'tb_dvalores_configuracion_persona',
            },
        ),
        migrations.CreateModel(
            name='TbDdatosContacto',
            fields=[
                ('id_datos_contacto', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('telefono', models.TextField(blank=True, null=True)),
                ('correo', models.TextField(blank=True, null=True)),
                ('fecha_registro', models.DateField(blank=True, null=True)),
                ('id_usuario_registro', models.ForeignKey(db_column='id_usuario_registro', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_ddatos_contacto',
            },
        ),
        migrations.CreateModel(
            name='TbDconfiguracionProceso',
            fields=[
                ('id_configuracion_proceso', models.AutoField(primary_key=True, serialize=False)),
                ('flujo', models.BooleanField(blank=True, null=True)),
                ('descripcion_configuracion_proceso', models.TextField(blank=True, null=True)),
                ('fecha_registro', models.DateField(blank=True, null=True)),
                ('id_usuario_registro', models.ForeignKey(db_column='id_usuario_registro', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_dconfiguracion_proceso',
            },
        ),
    ]