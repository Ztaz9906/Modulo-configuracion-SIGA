# Generated by Django 4.2.5 on 2023-10-11 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('autenticacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='id_provincia',
            field=models.ForeignKey(blank=True, db_column='id_provincia', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.tbnprovincia'),
        ),
    ]