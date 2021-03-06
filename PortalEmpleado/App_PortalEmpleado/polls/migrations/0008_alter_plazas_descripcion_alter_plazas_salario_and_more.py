# Generated by Django 4.0.5 on 2022-06-16 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_personas_correo_electronico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plazas',
            name='descripcion',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='plazas',
            name='salario',
            field=models.FloatField(max_length=70),
        ),
        migrations.CreateModel(
            name='Postulados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_postulacion', models.DateTimeField(verbose_name='fecha de postulación')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.personas')),
                ('plaza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.plazas')),
            ],
        ),
    ]
