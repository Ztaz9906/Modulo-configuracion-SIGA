# Generated by Django 4.1.3 on 2023-09-18 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cajero', '0007_alter_tbstructure_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbstructure',
            name='estructura_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cajero.tbstructure'),
        ),
    ]