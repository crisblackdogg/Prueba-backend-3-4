# Generated by Django 3.2.11 on 2022-12-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=70)),
                ('telefono', models.IntegerField()),
                ('fechaInscripcion', models.DateField()),
                ('hora', models.TimeField()),
                ('institucion', models.CharField(max_length=70)),
                ('estadoReserva', models.CharField(choices=[('reservado', 'RESERVADO'), ('completada', 'COMPLETADA'), ('anulada', 'ANULADA'), ('no asisten', 'NO ASISTEN')], max_length=70)),
                ('observacion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=70)),
            ],
        ),
    ]