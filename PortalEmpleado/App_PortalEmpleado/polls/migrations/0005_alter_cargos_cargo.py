# Generated by Django 4.0.5 on 2022-06-15 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_cargos_plazas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargos',
            name='cargo',
            field=models.CharField(max_length=100),
        ),
    ]