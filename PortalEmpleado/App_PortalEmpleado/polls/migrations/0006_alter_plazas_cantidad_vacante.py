# Generated by Django 4.0.5 on 2022-06-15 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_cargos_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plazas',
            name='cantidad_vacante',
            field=models.IntegerField(),
        ),
    ]
