# Generated by Django 4.2.5 on 2023-10-01 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cajero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbcategory',
            name='base',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
