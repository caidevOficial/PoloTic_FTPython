# Generated by Django 3.1.3 on 2020-12-02 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('ciudad', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion', models.IntegerField()),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arribos', to='Vuelos.aeropuerto')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidas', to='Vuelos.aeropuerto')),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('vuelos', models.ManyToManyField(blank=True, related_name='pasajeros', to='Vuelos.Vuelos')),
            ],
        ),
    ]
