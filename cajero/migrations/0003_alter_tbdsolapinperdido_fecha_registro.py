# Generated by Django 4.2.5 on 2023-10-12 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cajero', '0002_alter_tbdsolapinperdido_id_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbdsolapinperdido',
            name='fecha_registro',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
