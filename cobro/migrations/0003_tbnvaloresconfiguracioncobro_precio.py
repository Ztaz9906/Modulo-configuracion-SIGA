# Generated by Django 4.2.5 on 2023-10-18 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobro', '0002_tbnconfiguracioncobro_tbnvaloresconfiguracioncobro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbnvaloresconfiguracioncobro',
            name='precio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
