# Generated by Django 3.2.4 on 2021-07-20 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_barrio', models.CharField(max_length=100)),
                ('siglas', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=100)),
                ('cedula', models.IntegerField()),
                ('correo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_dept', models.CharField(max_length=100)),
                ('valor_dept', models.IntegerField()),
                ('cuartos_dept', models.IntegerField()),
                ('mensualidad', models.IntegerField()),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ubicacion_dept', to='administrativoCanton.barrio')),
                ('prop_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario_dept', to='administrativoCanton.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_casa', models.CharField(max_length=100)),
                ('valor_casa', models.IntegerField()),
                ('color', models.IntegerField()),
                ('cuartos_casa', models.IntegerField()),
                ('pisos', models.IntegerField()),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ubicacion_casa', to='administrativoCanton.barrio')),
                ('prop_casa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario_casa', to='administrativoCanton.persona')),
            ],
        ),
    ]
